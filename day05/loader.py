#!/usr/bin/env python
# -*- coding: utf-8 -*-

from seats import Seat


def read_input(filename="input"):
    with open('input', 'r') as f:
        for line in f.readlines():
            yield Seat(line.strip())
