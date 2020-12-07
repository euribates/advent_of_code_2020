#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Seat:

    def __init__(self, s):
        assert len(s) == 10
        self.row = int(s[0:7].translate({ord('F'): '0', ord('B'): '1'}), 2)
        self.column = int(s[7:10].translate({ord('L'): '0', ord('R'): '1'}), 2)
        self.seat_id = (self.row << 3) + self.column
