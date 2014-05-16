#!/usr/bin/env python

from setuptools import setup

setup(
    name='Xploration',
    version='1.0',
    description='Solar System Satellites Exploration',
    author='Chronos SpaceApps Rome Team 2014',
    author_email='@XplorationApp',
    url='http://www.spacexplore.it',
    install_requires=['djangorestframework==2.3.13', 'Django==1.6.2', 'django-cors-headers==0.12',
                      'django-rest-swagger==0.1.14', 'django-cms==3.0', 'django-classy-tags>=0.5',
                      'South==0.8.4', 'html5lib==1.0b1', 'django-mptt==0.6', 'django-sekizai==0.7',
                      'six==1.3.0', 'djangocms-admin-style==0.1.2', 'djangocms-text-ckeditor==2.1'],
)

