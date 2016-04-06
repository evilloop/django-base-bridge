# coding=utf-8
__author__ = 'Maple.Liu'
import importlib
import os
from base_bridge.utils.http import response_as_json
from api.settings import mosquitto_auth_np_path
import commands

def check_token_type(request, need_token_type):
    ret = {'code': 'OK'}
    if request.token_payload.get('type', '') != need_token_type:
        ret['code'] = 'TTNOTMATCH'
        return response_as_json(request, ret)


def get_settings():
    settings_module = os.environ['DJANGO_SETTINGS_MODULE']
    settings = importlib.import_module(settings_module)
    return settings


def make_topic_password(password):
    output = commands.getoutput('%s -p %s' % (mosquitto_auth_np_path, password))
    if output.startswith('PBKDF2$sha256$901'):
        return True, output
    else:
        return False, 'MOSQUITTO_MAKE_PASSWORD_CMD_ERROR'