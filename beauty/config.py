# -*- coding: utf8 -*-

import os
from os import path

proj_dir = path.dirname(path.dirname(path.abspath( __file__ )))
data_dir = path.join(proj_dir, 'data')
star_image_dir = path.join(data_dir, 'star_image')
star_face_dir = path.join(data_dir, 'star_face')
crop_face_dir = path.join(data_dir, 'crop_face')
star_features_p = path.join(data_dir, 'star_features.p')
star_encoding_p = path.join(data_dir, 'star_encoding.p')

feature_names = [
  'chin',
  'left_eyebrow',
  'right_eyebrow',
  'nose_bridge',
  'nose_tip',
  'left_eye',
  'right_eye',
  'top_lip',
  'bottom_lip'
]