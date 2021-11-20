#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/20/21 9:47 AM
# software: PyCharm

from sanic import Blueprint
from .user import user

user = Blueprint.group(user, url_prefix="user")
