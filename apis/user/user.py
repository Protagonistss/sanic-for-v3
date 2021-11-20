#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/20/21 9:13 AM
# software: PyCharm

from sanic import Blueprint, Request
from sanic_openapi import doc
from handler.auth import login_required
from schemas.auth import UserSubmitModel

user = Blueprint("user", url_prefix="account")


@user.post("regist")
@doc.consumes({"data": UserSubmitModel}, location="body")
@doc.summary("用户注册")
async def regist_user(request: Request):
    pass


@user.get("get")
@doc.summary("获取当前登录用户信息")
@login_required
async def get_user_info(request: Request):
    pass
