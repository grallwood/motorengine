#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from motorengine import __version__

tests_require = [
    'nose',
    'coverage',
    'rednose',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'mongoengine',
    'docutils',
    'jinja2',
    'sphinx',
]

setup(
    name='motorengine',
    version=__version__,
    description='MotorEngine is a port of the amazing MongoEngine Mapper. Instead of using pymongo, MotorEngine uses Motor.',
    long_description='''
MotorEngine is a port of the amazing MongoEngine Mapper. Instead of using pymongo, MotorEngine uses Motor.
''',
    keywords='database mongodb tornado python',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='http://github.com/heynemann/motorengine/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pymongo==3.6',
        'tornado==5.1.1',
        'motor==1.2.1',
        'six==1.11.0',
        'easydict==1.7'
    ],
    use_2to3=True,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
