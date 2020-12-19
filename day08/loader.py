#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import OP


def read_input(filename="sample"):
    with open(filename, "r") as f:
        for line in f:
            yield(OP(line))
