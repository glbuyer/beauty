# -*- coding: utf8 -*-

from beauty import config
from beauty import utils
from beauty.config import feature_names

from os import path
from scipy import ndimage
from urllib import request
import numpy as np
import cv2
import face_recognition
import json
import os
import pickle
import sys
import time
import traceback


def index_star(extract_function, outfile):
  image_files = []
  image_extensions = ['jfif', 'jpg', 'jpeg', 'png', 'JPG']
  star_image_dir = config.star_image_dir
  for par_dir, dirnames, filenames in os.walk(star_image_dir):
    if len(filenames) == 0:
      continue
    for filename in filenames:
      is_image = False
      for image_extension in image_extensions:
        if filename.endswith(image_extension):
          is_image = True
          break
      if not is_image:
        print('%s is not image' % (filename))
        continue
      image_file = path.join(par_dir, filename)
      image_files.append(image_file)
  print('#image=%d' % (len(image_files)))

  star_faces = {}
  for idx_image, image_file in enumerate(image_files):
    image = face_recognition.load_image_file(image_file)
    star_face = extract_function(image)
    num_image = idx_image + 1
    if (num_image % 10) == 0:
      print('#image=%d' % (num_image))
    star_name = utils.get_star_name(image_file)
    if star_face == None:
      print('fail %s' % (star_name))
    star_faces[star_name] = star_face
  pickle.dump(star_faces, open(outfile, 'wb'))


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
    result = match_star(image, save_image=save_image, verbose=verbose)
    response = utils.respond_success(result)
    # if verbose:
    #   duration = time.time() - start_time
    #   print('match star duration=%.4fs' % (duration))
    # print(json.dumps(response))
    # return response
  except Exception as e:
    message = traceback.format_exc()
    response = utils.respond_failure(message)
    # print(json.dumps(response))
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







