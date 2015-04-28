#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

classifiers = [
    "Framework :: Bottle",
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development']

description = "Hodge is a static blog generator in python"

url = 'https://github.com/avelino/hodge'

setup(name='hodge',
      version=0.1,
      description=description,
      long_description=description,
      classifiers=classifiers,
      keywords='staticblog blog generator',
      author="Thiago Avelino",
      author_email="thiago@avelino.xxx",
      url=url,
      download_url="{0}/tarball/master".format(url),
      license="MIT",
      install_requires=REQUIREMENTS,
      entry_points={
          'console_scripts': ["hodge = hodge:main"]
      },
      py_modules=['hodge'],
      scripts=['hodge.py'],
      include_package_data=True,
      zip_safe=False)
