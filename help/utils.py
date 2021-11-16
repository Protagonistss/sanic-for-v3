#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-18 18:42
# software: PyCharm
from functools import wraps

from PIL import Image
from scripts.fetch_images import gen_image_all_url
from os.path import abspath, dirname, join

ROOT_PATH = dirname(dirname(abspath(__file__)))


def resize_image(image_path: str, width: int, height: int, type='png', save_path='.'):
    image_ins = Image.open(image_path)
    out_ins = image_ins.resize((width, height), Image.ANTIALIAS)
    out_ins.save(gen_image_all_url(save_path), type)


def join_root_path(path: str):
    return join(dirname(dirname(abspath(__file__))), path)


def get_root_path():
    return dirname(dirname(abspath(__file__)))


def singleton(cls):
    _instances = {}

    @wraps(cls)
    def instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return instance


if __name__ == '__main__':
    resize_image('../images/0gax_1623912606234859.png', 100, 40)
