# -*- coding: utf8 -*-

import os
from os import path

proj_dir = path.dirname(path.dirname(path.abspath( __file__ )))
data_dir = path.join(proj_dir, 'data')
star_image_dir = path.join(data_dir, 'star_image')
star_face_dir = path.join(data_dir, 'star_face')
star_feature_p = path.join(data_dir, 'star_feature.p')

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