from sanic import Blueprint
from sanic.response import json
from sanic import Request
from sanic_openapi import doc
from schemas import UserSubmitModel
from sanic_jwt import exceptions

login = Blueprint("Login", url_prefix="/login")


@login.post('/submit')
@doc.consumes({"data": UserSubmitModel}, location="body")
async def user_login(request: Request):
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password")
    return json({
        "username": username,
        "password": password
    })
