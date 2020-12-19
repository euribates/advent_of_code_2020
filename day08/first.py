#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from machine import Proc


def main():
    proc = Proc()
    proc.load_memory(read_input('input'))
    proc.run()
    print(f"Solution 1: {proc.ACC}")


if __name__ == "__main__":
    main()
