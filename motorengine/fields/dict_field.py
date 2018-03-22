#!/usr/bin/env python
# -*- coding: utf-8 -*-

from motorengine.fields.base_field import BaseField


class DictField(BaseField):
    def to_son(self, value):
        return value

    def from_son(self, value):
        return value

    def validate(self, value):
        return True
