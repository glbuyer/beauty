# -*- coding: utf8 -*-

from setuptools import setup, find_packages

# pip install -Ue .
setup(
  name='beauty',
  author='Xiaojie Wang',
  packages=find_packages(),
  entry_points={
    'console_scripts': [
        'index=scripts:index',
        'match=scripts:match',
    ]
  },
)
