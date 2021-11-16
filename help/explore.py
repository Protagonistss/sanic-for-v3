#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-10 11:05
# software: PyCharm

import requests
from io import BytesIO


def identifyImage():
    url = 'http://127.0.0.1:5000/b'
    test_path = './images/0kez_16237737533395274.png'
    with open(test_path, "rb") as f:
        content = f.read()
    files = {'image_file': ('captcha.png', BytesIO(content), 'application')}
    print(files)
    r = requests.post(url=url, files=files)
    print(r)


if __name__ == '__main__':
    identifyImage()
