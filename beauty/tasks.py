# -*- coding: utf8 -*-

from beauty import config
from beauty import utils
from beauty.config import feature_names

from os import path
import numpy as np
import base64
import os
import json
import pickle
import time

def index_star():
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

  star_features = {}
  for idx_image, image_file in enumerate(image_files):
    star_name = path.basename(image_file)
    star_feature = utils.extract_feature(image_file, save_image=True)
    num_image = idx_image + 1
    if (num_image % 10) == 0:
      print('#image=%d' % (num_image))
    # if num_image >= 100:
    #   break
    if star_feature == None:
      print('fail %s' % (star_name))
    star_features[star_name] = star_feature
  # for star_name, image_feature in star_features.items():
  #   print(star_name, image_feature)
  pickle.dump(star_features, open(config.star_feature_p, 'wb'))

def match_star(image_file):
  start_time = time.time()

  # face_feature = utils.extract_feature(image_file, save_image=True)
  face_feature = utils.extract_feature(image_file, save_image=False)
  star_features = pickle.load(open(config.star_feature_p, 'rb'))

  chin_star = utils.search_star(face_feature, star_features, feature_names[0:1])
  # print('chin=%s' % (chin_star.split('.')[0]))
  eyebrow_star = utils.search_star(face_feature, star_features, feature_names[1:3])
  # print('eyebrow=%s' % (eyebrow_star.split('.')[0]))
  nose_star = utils.search_star(face_feature, star_features, feature_names[3:5])
  # print('nose=%s' % (nose_star.split('.')[0]))
  eye_star = utils.search_star(face_feature, star_features, feature_names[5:7])
  # print('eye=%s' % (eye_star.split('.')[0]))
  lip_star = utils.search_star(face_feature, star_features, feature_names[7:9])
  # print('lip=%s' % (lip_star.split('.')[0]))

  end_time = time.time()
  duration = end_time - start_time
  # print('duration=%.4fs' % (duration))

  result = {
    'chin': chin_star,
    'eyebrow': eyebrow_star,
    'nose': nose_star,
    'eye': eye_star,
    'lip': lip_star,
  }
  print(json.dumps(result))








