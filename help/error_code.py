#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/22/21 8:53 PM
# software: PyCharm
from enum import Enum


class ErrorCode(Enum):
    SUCCESS = 200


MapCodeToMsg = {
    200: 'success'
}
