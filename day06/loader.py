#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_input(filename="input"):
    with open(filename, 'r') as f:
        buff = []
        for line in f.readlines():
            line = line.strip()
            if line:
                buff.append(line)
            else:
                yield buff
                buff = []
        if buff:
            yield buff
