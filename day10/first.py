#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

from loader import read_input
from jolts import jolts_reduce


def main():
    devices = list(read_input('input'))
    stats = jolts_reduce(devices)
    assert len(stats) == 2
    sol = stats[1] * stats[3]
    print(f"Solution 1 is {sol}")


if __name__ == "__main__":
    main()
    


