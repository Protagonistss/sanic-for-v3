from sanic import Blueprint
from .login import login

auth = Blueprint.group(login, url_prefix="/auth")
