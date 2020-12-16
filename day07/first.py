#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from bags import Bag


def main():
    all_bags = list(read_input("input"))
    shiny_gold = Bag.registry[('shiny', 'gold')]
    acc = 0
    for bag in all_bags:
        if shiny_gold in bag.expand():
            acc += 1
    print(f"Solution 1: {acc}")


if __name__ == "__main__":
    main()
