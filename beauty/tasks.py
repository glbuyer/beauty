# -*- coding: utf8 -*-

from beauty import config
from beauty import utils
from beauty.config import feature_names

from os import path
from scipy import ndimage
from urllib import request
from sys import stdout
import numpy as np
import cv2
import face_recognition
import json
import operator
import os
import pickle
import sys
import time
import traceback
from PIL import Image


def index_star(extract_function, outfile, verbose=False):
  signature = 'tasks.index_star'

  image_files = utils.get_star_images()
  print('%s:#image=%d' % (signature, len(image_files)))

  star_faces = {}
  for idx_image, image_file in enumerate(image_files):
    star_name = utils.get_star_name(image_file)
    if verbose:
      print('%s:index %s' % (signature, star_name))
    image = face_recognition.load_image_file(image_file)
    star_face = extract_function(image, verbose=verbose)
    if star_face is None:
      print('%s:skip %s' % (signature, star_name))
      continue
    num_image = idx_image + 1
    if (num_image % 20) == 0:
      print('#image=%d' % (num_image))
    star_faces[star_name] = star_face
  pickle.dump(star_faces, open(outfile, 'wb'))


def posit_star():
  signature = 'tasks.posit_star'
  
  utils.create_dir(config.crop_face_dir)

  image_files = utils.get_star_images(path.join(config.data_dir, 'compress'))
  print('%s:#image=%d' % (signature, len(image_files)))

  for idx_image, image_file in enumerate(image_files):
    # print(path.basename(image_file))
    image = face_recognition.load_image_file(image_file)
    pimage = Image.fromarray(image)
    width, height = pimage.size
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) == 0:
      print(path.basename(image_file))
      continue
    face_location = face_locations[0]
    top, right, bottom, left = face_location
    center_x = (right + left) / 2.0
    center_y = (top + bottom) / 2.0
    half_width = (right - left) / 2.0
    half_height = (bottom - top) / 2.0
    scale = 2.1
    half_len = max(scale * half_width, scale * half_height)
    half_len = min(half_len, center_x - 0.0, width - center_x)
    half_len = min(half_len, center_y - 0.0, height - center_y)


    left, right = center_x - half_len, center_x + half_len
    top, bottom = center_y - half_len, center_y + half_len

    # print(left, top, right, bottom)
    pimage = pimage.crop((left, top, right, bottom))
    # pimage.show()
    filename = path.basename(image_file)
    filename = '%s.jpg' % filename.split('.')[0]
    outfile = path.join(config.crop_face_dir, filename)
    pimage.save(outfile)
    num_image = idx_image + 1
    if (num_image % 20) == 0:
      print('#image=%d' % (num_image))

def match_star_by_file(image_file, save_image=False, verbose=False):
  # print('match_star_by_file')
  try:
    start_time = time.time()
    image = face_recognition.load_image_file(image_file)
    if verbose:
      duration = time.time() - start_time
      print('load image file duration=%.4fs' % (duration))
  except Exception as e:
    message = traceback.format_exc()
    response = utils.respond_failure(message)
    # print(json.dumps(response))
    # return
    return response

  try:
    # start_time = time.time()
    # stdout.write('file=%s' % (path.basename(image_file)))
    result = match_star(image, save_image=save_image, verbose=verbose)

    dist_list = [star_dist['distance'] for _, star_dist in result.items()]
    dist = sum(dist_list)
    print('file=%s dist=%.4f' % (path.basename(image_file), dist))
    if dist <= 2.00:
      result['number'] = 5
    elif dist <= 2.38:
      result['number'] = 4
    elif dist <= 2.60:
      result['number'] = 3
    elif dist <= 2.80:
      result['number'] = 2
    else:
      result['number'] = 1

    response = utils.respond_success(result)
    # if verbose:
    #   duration = time.time() - start_time
    #   print('match star duration=%.4fs' % (duration))
    # print(json.dumps(response))
    # return response
  except Exception as e:
    message = traceback.format_exc()
    response = utils.respond_failure(message)
    # print(message)
    # print(json.dumps(response))
  # print(response)
  return response


def match_star_by_url(image_url):
  # print('match_star_by_url')
  # start_time = time.time()

  try:
    resp = request.urlopen(image_url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  except Exception as e:
    # print('asdfasdf')
    # traceback.print_exc()
    response = utils.respond_failure(str(e))
    print(json.dumps(response))
    return

  try:
    result = match_star(image)
    response = utils.respond_success(result)
    print(json.dumps(response))
  except Exception as e:
    print('asdfasdf')
    traceback.print_exc()
    response = utils.respond_failure(str(e))
    print(json.dumps(response))
    return

  # duration = time.time() - start_time
  # print('duration=%.4fs' % duration)


def match_star(image, verbose=False, save_image=False):
  star_encoding = pickle.load(open(config.star_encoding_p, 'rb'))
  face_encoding = utils.extract_encoding(image, verbose=verbose)
  from scipy.spatial import distance
  star_dist_dict = {}
  for star, encoding in star_encoding.items():
    dist = distance.euclidean(face_encoding, encoding)
    star_dist_dict[star] = dist
  star_dist_list = sorted(star_dist_dict.items(), key=operator.itemgetter(1))
  
  # dist_list = [dist for star, dist in star_dist_list]
  # dist = sum(dist_list) / len(dist_list)
  # stdout.write(' dist=%.4f\n' % dist)
  
  names = ['chin', 'eye', 'eyebrow', 'lip', 'nose']
  result = {}
  for name, star_dist in zip(names, star_dist_list):
    star, dist = star_dist
    result[name] = {
      'starname': star,
      'distance': dist,
    }
  # print(result)
  return result

  # face_feature = utils.extract_feature(image_file, save_image=True)
  # start_time = time.time()
  face_feature = utils.extract_feature(image, save_image=save_image, verbose=verbose)
  # if verbose:
  #   duration = time.time() - start_time
  #   print('match star extract feature duration=%.4fs' % (duration))

  star_features = pickle.load(open(config.star_feature_p, 'rb'))

  start_time = time.time()
  feat_dict = {}
  
  chin_feat = utils.search_star(face_feature, star_features, feature_names[0:1])
  # print('chin=%s' % (chin_star.split('.')[0]))
  feat_dict['chin'] = chin_feat
  
  eyebrow_feat = utils.search_star(face_feature, star_features, feature_names[1:3])
  # print('eyebrow=%s' % (eyebrow_star.split('.')[0]))
  feat_dict['eyebrow'] = eyebrow_feat

  nose_feat = utils.search_star(face_feature, star_features, feature_names[3:5])
  # print('nose=%s' % (nose_star.split('.')[0]))
  feat_dict['nose'] = nose_feat

  eye_feat = utils.search_star(face_feature, star_features, feature_names[5:7])
  # print('eye=%s' % (eye_star.split('.')[0]))
  feat_dict['eye'] = eye_feat

  lip_feat = utils.search_star(face_feature, star_features, feature_names[7:9])
  # print('lip=%s' % (lip_star.split('.')[0]))
  feat_dict['lip'] = lip_feat

  if verbose:
    duration = time.time() - start_time
    print('match star search star duration=%.4fs' % (duration))

  end_time = time.time()
  duration = end_time - start_time
  # print('duration=%.4fs' % (duration))

  result = {}
  for name, feat in feat_dict.items():
    starname, distance = feat
    result[name] = {
      'starname': starname,
      'distance': distance,
    }

  return result

  # outfile = path.join(path.expanduser('~'), 'result.txt')
  # with open(outfile, 'w') as fout:
  #   json.dump(result, fout)







