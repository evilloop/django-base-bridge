# coding=utf-8
__author__ = 'Maple.Liu'

import time
import json
from fields import *


class Model(raw_models.Model):
    class Meta:
        abstract = True

    # 序列化输出的字段
    output_fields = []

    # 时间日期格式
    datetime_format = '%Y-%m-%d %H:%m:%s'

    # 公共字段
    add_timestamp = BigIntegerField(verbose_name=u'入库时间', default=time.time)
    update_timestamp = BigIntegerField(verbose_name=u'更新时间', default=time.time)

    def as_dict(self, keys=None):
        if not keys:
            keys = self.output_fields
        object_dict = dict()
        for key in keys:
            value = last_value = getattr(self, key)
            if isinstance(value, models.Model):
                if isinstance(value, self.__class__):
                    last_value = value.__unicode__()
                else:
                    last_value = value.as_dict()
            object_dict[key] = last_value
        return object_dict

    def as_json(self, keys=None):
        return json.dumps(self.as_dict(keys))

    def get_add_time(self):
        return time.strftime(self.datetime_format, time.localtime(self.add_timestamp))
    get_add_time.allow_tags = True
    get_add_time.short_description = u'添加时间'

    def get_update_time(self):
        return time.strftime(self.datetime_format, time.localtime(self.update_timestamp))
    get_update_time.allow_tags = True
    get_update_time.short_description = u'更新时间'