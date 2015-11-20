# coding=utf-8

import os
import importlib

__author__ = 'Maple.Liu'


def get_settings():
    settings_module = os.environ['DJANGO_SETTINGS_MODULE']
    settings = importlib.import_module(settings_module)
    return settings
