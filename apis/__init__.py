from sanic import Blueprint
from .train import train

apis = Blueprint.group(train, url_prefix="/api")
