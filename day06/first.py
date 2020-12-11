#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from answers import AnyAnswer

acc = 0
for responses in read_input('input'):
    acc += len(AnyAnswer(responses))

print(f"Solution 1: {acc}")
