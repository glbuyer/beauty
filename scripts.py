# -*- coding: utf8 -*-

from beauty import tasks

from argparse import ArgumentParser

def index():
  tasks.index_star()

def match():
  parser = ArgumentParser()
  parser.add_argument('image_file', type=str)
  args = parser.parse_args()

  image_file = args.image_file
  tasks.match_star(image_file)






