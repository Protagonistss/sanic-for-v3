from sanic import Blueprint
from .auth import train

apis = Blueprint.group(train, url_prefix="/api")
