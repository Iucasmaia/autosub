#!/usr/bin/env python
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = (
    'Autosub is a utility for automatic speech recognition and subtitle generation. '
    'It takes a video or an audio file as input, performs voice activity detection '
    'to find speech regions, makes parallel requests to Speech Recognition API to '
    'generate transcriptions for those regions, (optionally) translates them to a '
    'different language, and finally saves the resulting subtitles to disk. '
    'It supports a variety of input and output languages (to see which, run the '
    'utility with --list-src-languages and --list-dst-languages as arguments '
    'respectively) and can currently produce subtitles in either the SRT format or '
    'simple JSON.'
)

setup(
    name='autosubmaia',
    version='0.0.1',
    description='Auto-generates subtitles for any video or audio file with support to wit.ai and speech recognition module.',
    long_description=long_description,
    author='Lucas Maia',
    author_email='lucasmaia.contato@icloud.com',
    url='https://github.com/Iucasmaia/autosub',
    packages=['autosub'],
    entry_points={
        'console_scripts': [
            'autosub = autosub:main',
        ],
    },
    install_requires=[
        'google-api-python-client>=1.4.2',
        'requests>=2.3.0',
        'pysrt>=1.0.1',
        'progressbar2>=3.34.3',
        'six>=1.11.0',
        'SpeechRecognition>=3.8.1',
    ],
    license=open("LICENSE").read()
)
