#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bag:

    registry = {}

    def __init__(self, kind, color):
        self.kind = kind
        self.color = color
        self.contains = []

    def name(self):
        return f"{self.kind}/{self.color}"

    def __str__(self):
        buff = [f"{self.kind}/{self.color} --> ["]
        sep = ''
        for sb, num in self.contains:
            buff.append(sep)
            buff.append(f"{num} x {sb.kind}/{sb.color}")
            sep = " | "
        buff.append("]")
        return ''.join(buff)

    def __eq__(self, other):
        return all([
            self.kind == other.kind,
            self.color == other.color,
            ])

    def __hash__(self):
        return hash((self.kind, self.color))

    def expand(self):
        result = set([])
        for subbag, _ in self.contains:
            result.add(subbag)
            result = result.union(subbag.expand())
        return result

    def count(self, acc=0):
        if not self.contains:
            return 1
        else:
            return acc + sum([
                (subbag.count(acc=1) * num)
                for subbag, num in self.contains
                ]) 
                  
            
