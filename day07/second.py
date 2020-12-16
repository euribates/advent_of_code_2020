#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from bags import Bag


def main():
    list(read_input("input"))
    shiny_gold = Bag.registry[('shiny', 'gold')]
    print(f"Solution 2: {shiny_gold.count()}")


if __name__ == "__main__":
    main()
