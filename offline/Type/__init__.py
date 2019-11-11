#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File      : __init__.py
@Time      : 2019/11/11
@Author    : Iydon Liang
@Contact   : liangiydon@gmail.com
@Docstring : Initialize the `Type` module.
'''

from . import latex, models


_types = ('不定项选择', '纵向不定项选择', '不定数填空')
__import__(f'{__package__}.models', fromlist=_types)
types = {_type: getattr(models, _type) for _type in _types}
