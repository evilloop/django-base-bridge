# coding=utf-8

from django.http import HttpResponse
import json
import django
from api.settings import logger
from api.settings import client

__author__ = 'Maple.Liu'


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
    if django.get_version() >= '1.6':
        response = HttpResponse(content_type="application/json")
    else:
        response = HttpResponse(mimetype='application/json')
    res = json.dumps(obj)
    response.write(res)
    if 'Access-Control-Allow-Origin' not in headers.keys():
        headers['Access-Control-Allow-Origin'] = '*'
    for k, v in headers.items():
        response[k] = v
    if before_response is not None:
        before_response(request)
    if obj['code'] != 'OK':
        event_type = 'raven.events.Message'
        message = obj.get('msg', '无消息')
        client.capture(event_type=event_type, message=message, request=request)
    return response
