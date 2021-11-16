from sanic import Blueprint
from .image import image

train = Blueprint.group(image, url_prefix="/train")
