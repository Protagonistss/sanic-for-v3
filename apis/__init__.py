from sanic import Blueprint
from .auth import login

apis = Blueprint.group(login, url_prefix="/api")
