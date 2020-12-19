#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from itertools import islice, permutations


class Decoder:

    def __init__(self, size=25, preamble=None):
        self.size = size
        self.items = deque([], self.size)
        if preamble is not None:
            self.load_preamble(preamble)

    def load_preamble(self, stream):
        self.items.extend(islice(stream, self.size))
        assert len(self.items) == self.size

    def append(self, value):
        self.items.append(value)

    def possible_next_values(self) -> set:
        return set(a+b for a, b in permutations(self.items, 2))

    def is_valid(self, next_value):
        return next_value in self.possible_next_values()
