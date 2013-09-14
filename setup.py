#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from ask import __version__


CLASSIFIERS = [
]

setup(
    name='ask',
    version=__version__,
    description='Easy input validation for python',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Kim Thoenen',
    author_email='kim@smuzey.ch',
    url='https://github.com/chive/ask',
    packages=find_packages(),
    license='MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
)