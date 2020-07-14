# coding; utf-8

import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    JSON_SORT_KEYS = False
    APPLICATION_ROOT = '/api'
    SECRET_KEY = environ.get('SECRET_KEY')
    DB_USER = 'postgres'
    DB_PASS = 'admin'
    DB_NAME = 'casa_js'
    DB_HOST = 'database'
    DB_PORT = 5432


class Development(Config):
    debug = True


config_meta = {
    'default': Config,
    'dev': Development
}
