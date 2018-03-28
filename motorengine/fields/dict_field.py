#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from motorengine.fields.base_field import BaseField


class DictField(BaseField):
    def to_son(self, value):
        return value

    def from_son(self, value):
        return value

    def validate(self, value):
        if type(value) is not dict:
            return False
        for key in value.keys():
            if type(key) is not str:
                return False

        try:
            json.dumps(value)
        except TypeError:
            return False

        return True
