# coding=utf-8

from django.db import models

__author__ = 'Maple.Liu'


class AutoField(models.AutoField):
    def __init__(self, *args, **kwargs):
        super(AutoField, self).__init__(*args, **kwargs)


class BigIntegerField(models.BigIntegerField):
    def __init__(self, *args, **kwargs):
        super(BigIntegerField, self).__init__(*args, **kwargs)


class BinaryField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        super(BinaryField, self).__init__(*args, **kwargs)


class BooleanField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['default'] = False
        super(BooleanField, self).__init__(*args, **kwargs)


class CharField(models.CharField):
    def __init__(self, max_length=1024, *args, **kwargs):
        kwargs['max_length'] = max_length
        super(CharField, self).__init__(*args, **kwargs)


class CommaSeparatedIntegerField(models.CommaSeparatedIntegerField):
    def __init__(self, *args, **kwargs):
        super(CommaSeparatedIntegerField, self).__init__(*args, **kwargs)


class DateField(models.DateField):
    def __init__(self, *args, **kwargs):
        super(DateField, self).__init__(*args, **kwargs)


class DateTimeField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        super(DateTimeField, self).__init__(*args, **kwargs)


class DecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        super(DecimalField, self).__init__(*args, **kwargs)


class EmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        super(EmailField, self).__init__(*args, **kwargs)


class FileField(models.FileField):
    def __init__(self, *args, **kwargs):
        super(FileField, self).__init__(*args, **kwargs)


class FilePathField(models.FilePathField):
    def __init__(self, *args, **kwargs):
        super(FilePathField, *args, **kwargs)


class FloatField(models.FloatField):
    def __init__(self, *args, **kwargs):
        super(FloatField, self).__init__(*args, **kwargs)


class ImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        super(ImageField, self).__init__(*args, **kwargs)


class IntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super(IntegerField, self).__init__(*args, **kwargs)


class IPAddressField(models.IPAddressField):
    def __init__(self, *args, **kwargs):
        super(IPAddressField, self).__init__(*args, **kwargs)


class GenericIPAddressField(models.GenericIPAddressField):
    def __init__(self, *args, **kwargs):
        super(GenericIPAddressField, self).__init__(*args, **kwargs)


class NullBooleanField(models.NullBooleanField):
    def __init__(self, *args, **kwargs):
        super(NullBooleanField, self).__init__(*args, **kwargs)


class PositiveIntegerField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        super(PositiveIntegerField, self).__init__(*args, **kwargs)


class PositiveSmallIntegerField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        super(PositiveSmallIntegerField, self).__init__(*args, **kwargs)


class SlugField(models.SlugField):
    def __init__(self, *args, **kwargs):
        super(SlugField, self).__init__(*args, **kwargs)


class SmallIntegerField(models.SmallIntegerField):
    def __init__(self, *args, **kwargs):
        super(SmallIntegerField, self).__init__(*args, **kwargs)


class TextField(models.TextField):
    def __init__(self, null=True, blank=True, *args, **kwargs):
        kwargs['null'] = null
        kwargs['blank'] = blank
        super(TextField, self).__init__(*args, **kwargs)


class TimeField(models.TimeField):
    def __init__(self, *args, **kwargs):
        super(TimeField, self).__init__(*args, **kwargs)


class URLField(models.URLField):
    def __init__(self, max_length=1024, *args, **kwargs):
        kwargs['max_length'] = max_length
        super(URLField, self).__init__(*args, **kwargs)


class ForeignKey(models.ForeignKey):
    def __init__(self, to, to_field=None, **kwargs):
        super(ForeignKey, self).__init__(to, to_field, **kwargs)


class ManyToManyField(models.ManyToManyField):
    def __init__(self, to, **kwargs):
        super(ManyToManyField, self).__init__(to, **kwargs)


class OneToOneField(models.OneToOneField):
    def __init__(self, to, to_field=None, **kwargs):
        super(OneToOneField, self).__init__(to, to_field=None, **kwargs)