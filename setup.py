#!/usr/bin/env python

from setuptools import setup

setup(
    name='Chronos',
    version='1.0',
    description='Solar System Satellites Xploration!',
    author='Chronos SpaceApps Rome Team 2014',
    author_email='https://2014.spaceappschallenge.org/project/chronos/',
    url='http://www.spacexplore.it',
    install_requires=['djangorestframework==2.3.13', 'Django==1.6.2', 'django-cors-headers==0.12',
                      'django-rest-swagger==0.1.14'],
)

