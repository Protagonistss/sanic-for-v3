from sanic import Blueprint
from sanic.response import json
from sanic import Request
from sanic_openapi import doc
from schemas import UserSubmitModel
from handler.auth import gen_token
import datetime

login = Blueprint("auth", url_prefix="/login")


@login.post('/submit')
@doc.consumes({"data": UserSubmitModel}, location="body")
async def user_login(request: Request):
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    token = gen_token(payload={"exp": datetime.datetime.now() + datetime.timedelta(days=1),
                               "iat": datetime.datetime.now(), },
                      data={"username": username, "password": password})
    return json({
        "code": 200,
        "data": {
            "token": token
        }
    })
