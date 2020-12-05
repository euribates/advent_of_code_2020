#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Karte:

    def __init__(self, filename='input'):
        self.kernel = dict()
        with open(filename, 'r') as f:
            for y, line in enumerate(f.readlines()):
                for x, char in enumerate(line.strip()):
                    self.kernel[(x, y)] = char
        self.width = x + 1
        self.height = y + 1

    def __getitem__(self, pos):
        x, y = pos
        x = x % self.width
        y = y % self.height
        return self.kernel[(x, y)]

    def print(self, max_x=None, max_y=None):
        max_x = max_x or self.width
        max_y = max_y or self.height
        for y in range(max_y):
            for x in range(max_x):
                pos = (x, y)
                print(self[pos], end='', sep='')
            print()
