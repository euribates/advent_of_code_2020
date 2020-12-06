#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from rules import is_full_passport


def main():
    result = 0
    for passport in read_input('input'):
        if is_full_passport(passport):
            result += 1
    print(f"Solution 1: {result}")


if __name__ == "__main__":
    main()
