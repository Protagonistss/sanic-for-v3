#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/19/21 7:21 PM
# software: PyCharm
from help.error_code import MapCodeToMsg


class ResponseHandler:

    @classmethod
    def to_dict(cls, code: int, msg: any = None, data={}):
        if msg:
            return {"code": code, "msg": msg, "data": data}
        else:
            return {"code": code, "msg": MapCodeToMsg.get(code, 200), "data": data}
