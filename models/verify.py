#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-06-21 22:49
# software: PyCharm

from tortoise import Model
from tortoise import fields


class Verify(Model):
    id = fields.UUIDField(pk=True)
    initial_prefix = fields.TextField()
    identify_prefix = fields.TextField()
    suffix = fields.TextField()

    class Meta:
        table = "verify"

    def __repr__(self):
        return '验证码{}_{}'.format(self.initial_prefix, self.suffix)
