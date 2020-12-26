#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import functools


def device_jolts(adapters):
    return max(adapters) + 3


def jolts_reduce(adapters):
    stats = collections.Counter()
    adapters.sort()
    finish = device_jolts(adapters)
    adapters.append(finish)

    def calculate(a, b):
        key = b - a
        stats[key] += 1
        return b

    functools.reduce(calculate, adapters, 0)
    return stats


# Part 2

def next_options(adapters, value):
    return [
        j for j in adapters if j > value
        ][0:3]


@functools.lru_cache
def alternative_paths(length):
    if length < 2:
        return 1
    elif length == 2:
        return 2
    elif length == 3:
        return 4
    elif length == 4:
        return 7
    return sum([
        alternative_paths(length-1),
        alternative_paths(length-2),
        alternative_paths(length-3),
        ])


