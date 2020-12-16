#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bags import Bag

EOL = '\n'


def load_names(filename):
    kinds = set()
    colors = set()
    with open(filename, "r") as f:
        for line in f.readlines():
            kind, color, *resto = line.split()
            kinds.add(kind)
            colors.add(color)
    return kinds, colors


def get_kind(tokenizer, kinds):
    token = next(tokenizer)
    assert token in kinds
    return token


def get_color(tokenizer, colors):
    token = next(tokenizer)
    assert token in colors
    return token


def literal_bag(tokenizer):
    pat_bag = re.compile('bags?[.,]?')
    token = next(tokenizer)
    assert pat_bag.match(token)


def literal(tokenizer, text):
    token = next(tokenizer)
    assert token == text, f"Waiting for {text}, got {token} instead."


def load_bag(tokenizer, kinds, colors):
    kind = get_kind(tokenizer, kinds)
    color = get_color(tokenizer, colors)
    bag = Bag.registry[(kind, color)]
    literal(tokenizer, "bags")
    literal(tokenizer, "contain")
    token = next(tokenizer)
    if token == 'no':
        literal(tokenizer, "other")
        literal(tokenizer, "bags.")
        literal(tokenizer, EOL)
    else:
        while token != EOL:
            num = int(token)
            kind = get_kind(tokenizer, kinds)
            color = get_color(tokenizer, colors)
            literal_bag(tokenizer)
            new_bag = Bag.registry[(kind, color)]
            bag.contains.append((new_bag, num))
            token = next(tokenizer)
    return bag


class Tokenizer:

    def __init__(self, line):
        self.line = line
        self.items = self.line.split()
        self.count = len(self.items)
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < self.count:
            result = self.items[self.index]
            self.index += 1
            return result
        return EOL
        raise StopIteration


def read_input(filename="input"):
    kinds, colors = load_names(filename)
    Bag.registry.update({
        (k, c): Bag(k, c)
        for k in kinds
        for c in colors
        })
    with open(filename, "r") as f:
        for line in f:
            tokenizer = Tokenizer(line)
            bag = load_bag(tokenizer, kinds, colors)
            yield bag
