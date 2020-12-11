#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from answers import AllAnswer

acc = 0
for responses in read_input('input'):
    acc += len(AllAnswer(responses))

print(f"Solution 2: {acc}")
