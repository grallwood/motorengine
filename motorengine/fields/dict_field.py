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
        if isinstance(value, (dict, list)):
            return False
        for key in value.keys():
            if not isinstance(key, str):
                return False

        try:
            json.dumps(value)
        except Excepetion as e:
            return False

        return True
