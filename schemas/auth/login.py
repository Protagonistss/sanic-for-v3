#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/18/21 7:23 PM
# software: PyCharm

from sanic_openapi import doc


class UserSubmitModel:
    username: str
    password: str


# class UserSubmit:
#     doc.Object(UserSubmitModel)
