#!/usr/bin/env python
# -*- coding: utf-8 -*-


from karte import Karte


def read_input(filename='sample'):
    result = Karte()
    with open(filename, 'r') as stream:
        for y, line in enumerate(stream):
            line = line.strip()
            for x, char in enumerate(line):
                result[(x, y)] = char
    return result
