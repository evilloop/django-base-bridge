# coding=utf-8

import codecs
import os

__author__ = 'Maple.Liu'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    with codecs.open(os.path.join(os.path.dirname(__file__), filename)) as fileobject:
        return fileobject.read()

NAME = 'base_bridge'

PACKAGES = ['base_bridge', ]

DESCRIPTION = "A base bridge between django framework and our private application."

LONG_DESCRIPTION = read('README.md')

KEYWORDS = "django base bridge model field db"

AUTHOR = "Maple.Liu"

AUTHOR_EMAIL = "fjliufeng@163.com"

URL = "https://github.com/evilloop/django-base-bridge"

VERSION = "0.0.1"

LICENSE = "GNU GENERAL PUBLIC LICENSE"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
