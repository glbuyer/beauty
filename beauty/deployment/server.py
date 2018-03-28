# -*- coding: utf8 -*-

from beauty import tasks
from beauty import utils

from sys import path
from flask import Flask
from flask import jsonify, render_template, request
import json
import site
import string

server = Flask(__name__)

@server.route('/', methods=['POST'])
def index():
  signature = 'server.index'
  content_type = request.headers['Content-Type']
  if content_type == 'application/json':
    data = request.get_json()
  else:
    data = request.form
  if 'image_file' not in data:
    message = '%s:no image file specified' % signature
    response = utils.respond_failure(message)
    return jsonify(response)
  image_file = data['image_file']
  response = tasks.match_star_by_file(image_file)
  return jsonify(response)


# python server.py
if __name__ == '__main__':
    # server.run(host='0.0.0.0', port=3000, threaded=True)
    server.run(debug=True, port=3000, threaded=True)