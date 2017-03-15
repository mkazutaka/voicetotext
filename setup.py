# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('Readme.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
        name='voicetotext',
        version='1.0.1',
        url='https://github.com/kztka/voicetotext',
        author='kztka',
        author_email='paper.sheet.kami@gmail.com',
        maintainer='kztka',
        maintainer_email='paper.sheet.kami@gmail.com',
        description='Transript media file to text using google api.',
        long_description=readme,
        packages=find_packages(),
        py_modules=['voicetotext'],
        install_requires=_requires_from_file('requirements.txt'),
        license="MIT",
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approved :: MIT License',
        ],
        entry_points='''
            # -*- Entry points: -*-
            [console_scripts]
            voicetotext=voicetotext.voicetotext:cli
            splitvoice=voicetotext.splitvoice:cli
        ''',
        )
