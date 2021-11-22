#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/21/21 5:03 PM
# software: PyCharm

from functools import wraps
from sanic import Request, exceptions, response
from sanic.handlers import ErrorHandler


class CustomErrorHandler(ErrorHandler):
    def default(self, request: Request, exception):
        print('request', request)
        print('exception', type(exception), exception)
        return super().default(request, exception)


async def server_error_handler(request: Request, exception):
    return response.json({"code": 500, "msg": "Internal Server Error"}, status=200)
