#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-21 11:35
# software: PyCharm

from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.UUIDField(pk=True)
    username = fields.TextField()
    email = fields.TextField()
    nickname = fields.TextField()

    class Meta:
        table = "user"

    def __repr__(self):
        return "User(id='{}')".format(self.id)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email, "nickname": self.nickname}
