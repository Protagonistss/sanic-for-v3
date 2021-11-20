#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 11/20/21 9:13 AM
# software: PyCharm

from sanic import Blueprint, Request
from sanic_openapi import doc
from handler.auth import login_required

user = Blueprint("user", url_prefix="account")


@user.get("get")
@doc.consumes("", location="query")
@login_required
async def get_user_info(request: Request):
    pass
