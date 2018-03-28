# -*- coding: utf8 -*-

from beauty import tasks

from argparse import ArgumentParser
import json

def index():
  tasks.index_star()

def match():
  parser = ArgumentParser()
  parser.add_argument('--image_file', type=str)
  parser.add_argument('--image_url', type=str)
  parser.add_argument('--verbose', action='store_true')
  args = parser.parse_args()

  if args.image_file:
    tasks.match_star_by_file(args.image_file, verbose=args.verbose)
  elif args.image_url:
    tasks.match_star_by_url(args.image_url)
  else:
    print(json.dumps({'scripts.match':'cannot handle'}))






