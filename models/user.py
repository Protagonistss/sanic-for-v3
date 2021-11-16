#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-21 11:35
# software: PyCharm

from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    mobile = fields.IntField()
    nickname = fields.TextField()

    def __str__(self):
        return '用户{}已经创建，手机号为{}'.format(self.name, self.mobile)
