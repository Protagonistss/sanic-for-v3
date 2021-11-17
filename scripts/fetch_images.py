import sys
import os

sys.path.append(os.pardir)

import random
import time
import requests
from contextlib import closing
from help import utils
from threading import Thread


def get_train_set_path(path: str):
    create_path = utils.join_root_path(path)
    return create_path


def create_train_set_dir(path='auth-set'):
    create_path = get_train_set_path(path)
    is_existed = os.path.exists(create_path)
    if not is_existed:
        os.mkdir(create_path)


def gen_image_name(char_pool):
    prefix = ''
    for i in range(4):
        prefix += random.choice(char_pool)
    suffix = str(time.time()).replace('.', '')
    return "{}_{}".format(prefix, suffix)


def gen_image_all_url(path):
    rule = '0123456789'
    return '{}/{}.png'.format(path, gen_image_name(rule))


def get_image(url, count=20000, path='auth-set'):
    create_train_set_dir(path)
    for loop in range(count):
        response = requests.get(url, verify=False, stream=True)
        with closing(response) as response:
            with open(gen_image_all_url(get_train_set_path(path)), 'wb') as f:
                for i in response.iter_content(chunk_size=512):
                    f.write(i)
        print('第{}张图片保存成功'.format(loop + 1))


def main():
    get_image('https://gray.930pm.cn/home.php/Login/verify_c', path='auth-set')


if __name__ == '__main__':
    t1 = Thread(target=main)
    t2 = Thread(target=main)
    t3 = Thread(target=main)
    t4 = Thread(target=main)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
