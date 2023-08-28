#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_caioesr',
      version='0.0.1',
      author='Caio Emmanuel',
      author_email='caioemmanuelsr@gmail.com',
      url='https://github.com/cemmanuelsr/cuddly-octo-potato',
      python_requires='>=3.9',
      platforms=['linux_x86_64'],
      install_requires=['requests'],
      scripts=['scripts/hello.py'],
      packages=['dev_aberto']
      )
