from sanic import Blueprint
from .login import login

login = Blueprint.group(login, url_prefix="/auth")
