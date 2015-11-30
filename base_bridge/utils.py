# coding=utf-8

import os
import importlib
from django.http import HttpResponse
import json

__author__ = 'Maple.Liu'


def get_settings():
    settings_module = os.environ['DJANGO_SETTINGS_MODULE']
    settings = importlib.import_module(settings_module)
    return settings


def response_as_json(request, obj, headers=dict(), before_response=None):
    """
    - 将一个Py对象转成JSON，构造返回HttpResponse
    - headers是由Http Header键值对组成的字典
    - before_response 是回调函数，发送响应数据之前要执行的操作

    def my_bofore_response(request):
        print request
        pass

    - response_as_json(request, {'data':'test'}, headers={}, before_response=my_before_response) => HttpResponse
    """
    response = HttpResponse(mimetype="application/json")
    res = json.dumps(obj)
    response.write(res)
    if 'Access-Control-Allow-Origin' not in headers.keys():
        headers['Access-Control-Allow-Origin'] = '*'
    for k, v in headers.items():
        response[k] = v
    if before_response is not None:
        before_response(request)
    return response
