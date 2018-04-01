# -*- coding: utf8 -*-

from beauty import config
from beauty import tasks
from beauty import utils

from argparse import ArgumentParser
import json


def index():
  parser = ArgumentParser()
  parser.add_argument('-f', '--features', action='store_true')
  parser.add_argument('-e', '--encoding', action='store_true')
  args = parser.parse_args()
  print('features=%s encoding=%s' % (args.features, args.encoding))

  if args.features:
    extract_function = getattr(utils, 'extract_features')
    tasks.index_star(extract_function, config.star_features_p)

  if args.encoding:
    extract_function = getattr(utils, 'extract_encoding')
    tasks.index_star(extract_function, config.star_encoding_p)


def match():
  parser = ArgumentParser()
  parser.add_argument('--image_file', type=str)
  parser.add_argument('--image_url', type=str)
  parser.add_argument('--save_image', action='store_true')
  parser.add_argument('--verbose', action='store_true')
  args = parser.parse_args()

  if args.image_file:
    save_image, verbose = args.save_image, args.verbose
    tasks.match_star_by_file(args.image_file, save_image=save_image, verbose=verbose)
  elif args.image_url:
    tasks.match_star_by_url(args.image_url)
  else:
    print(json.dumps({'scripts.match':'cannot handle'}))






