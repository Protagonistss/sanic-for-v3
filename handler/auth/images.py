from help.utils import join_root_path
from os import path, walk


async def get_images():
    train_set_path = join_root_path('auth-set')
    is_existed = path.exists(train_set_path)
    if is_existed:
        image_list = []
        for _, _, images in walk(train_set_path):
            image_list = images
        return image_list

    return []
