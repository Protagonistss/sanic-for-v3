from sanic import Blueprint
from sanic.response import json
from help.utils import join_root_path
from handler.auth import get_images
from models.verify import Verify
from sanic import Request
from sanic_openapi import doc
from schemas import PutVerify
from json import loads
import random

image = Blueprint("train_image", url_prefix="/images")
image.static('/static', join_root_path('auth-set'))


@image.get('/get')
@doc.consumes(doc.Integer(name="pageSize"))
async def get_verify_code(request: Request):
    query_args = request.args
    page_size = int(query_args.get("pageSize", 12))
    verifys = await Verify.filter(identify_prefix="").all().values()
    # TODOO
    count = await Verify.all().values()
    _verifys = []
    if len(verifys) > page_size:
        point = page_size
    else:
        point = len(verifys)
    while True:
        if len(_verifys) >= point:
            break
        item = random.randint(0, len(verifys) - 1)
        if item not in _verifys:
            _verifys.append(item)
    new_verifys = [verifys[i] for i in _verifys]
    images = []
    for verify in new_verifys:
        item = {"id": str(verify.get("id")),
                "identifyPrefix": verify.get("identify_prefix", None),
                "verifyUrl": "/api/auth/images/static/{}_{}".format(verify.get("initial_prefix"),
                                                                     verify.get("suffix"))}
        images.append(item)
    return json(
        {"data": {"images": images, "count": len(count), "surplus": len(verifys), "already": len(count) - len(verifys)},
         "msg": "success"}, 200)


@image.get('/typein')
async def type_in_verify(request):
    """
    just type in verify code once
    :param request:
    :return:
    """
    image_list = await get_images()
    needCreate = []
    for image in image_list:
        [prefix, suffix] = image.split('_')
        item = {"initial_prefix": prefix, "suffix": suffix, "identify_prefix": ''}
        needCreate.append(item)
    result = [Verify(**item) for item in needCreate]
    await Verify.bulk_create(result)
    return json({"data": {}, "msg": "success"}, 200)


@image.put('/identity')
@doc.consumes(PutVerify, location="body")
async def identity_image_name(request: Request):
    body = loads(request.body)
    identifyList = body.get("identifyList", [])
    count = len(identifyList)
    while count:
        identify = identifyList[count - 1]
        char = identify.get('identifyPrefix')
        count -= 1
        if not char:
            continue
        if len(char) != 4:
            continue
        await Verify.filter(id=identify.get("id", None)).update(identify_prefix=identify.get("identifyPrefix", None))
    return json({"data": {}, "msg": "success"}, 200)
