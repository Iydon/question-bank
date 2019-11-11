#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File      : __init__.py
@Time      : 2019/11/11
@Author    : Iydon Liang
@Contact   : liangiydon@gmail.com
@Docstring : Initialize the `Type` module.
'''

from . import latex


_types = ('不定项选择', '纵向不定项选择')
__import__(__package__, fromlist=_types)
_locals = locals()

types = {_tag: _locals[_tag] for _tag in _types}
