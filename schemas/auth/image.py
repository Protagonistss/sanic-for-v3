#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-22 23:13
# software: PyCharm
from sanic_openapi import doc


class SwaggerVerify:
    id = str
    identifyPrefix = str


class PutVerify:
    identifyList = doc.List(SwaggerVerify)
