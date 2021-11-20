from sanic import Blueprint
from .auth import auth
from .user import user

apis = Blueprint.group(auth, user, url_prefix="/api")
