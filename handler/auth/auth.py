#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/19/21 6:54 PM
# software: PyCharm

from functools import wraps
from sanic import Request, response
import jwt
from conf.settings import JWT

SECRET = "^*secret*#$98@!6$"


def gen_token(payload: dict, data: dict):
    return jwt.encode(dict(payload, **data), JWT.get("SECRET", SECRET), algorithm="HS256")


def check_toke(request: Request):
    try:
        jwt.decode(request.token, JWT.get("SECRET", SECRET), algorithms=["HS256"])
    except jwt.exceptions.InvalidTokenError:
        return False
    return True


def login_required(wrapper):
    def decorator(mid):
        @wraps(mid)
        async def decorator_wrapper(request, *args, **kwargs):
            is_auth = check_toke(request)
            if is_auth:
                res = mid(request, *args, **kwargs)
                return res
            else:
                return response.json({"code": 401, "msg": "token is invalid"}, 200)

        return decorator_wrapper

    return decorator(wrapper)
