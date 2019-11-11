#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File      : main.py
@Time      : 2019/11/11
@Author    : Iydon Liang
@Contact   : liangiydon@gmail.com
@Docstring : <no docstring>
'''

import json
from Type import types, latex


with open('data.json', 'r') as f:
    data = json.load(f)


# let it crash
text = [None] * len(data)
TeX = latex.api()
for ith, question in enumerate(data):
    _type = question.pop('type')
    api = types.get(_type).api(question)
    text[ith] = api.render()

result = TeX.render('\n'.join(text))

with open('result.tex', 'w') as f:
    f.write(result)
