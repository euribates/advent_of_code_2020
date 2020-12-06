#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from rules import is_valid_passport, is_full_passport


def main():
    result = 0
    for passport in read_input("input"):
        if is_full_passport(passport) and is_valid_passport(passport):
            result += 1
    print(f"Solution 2: {result}")


if __name__ == "__main__":
    main()
