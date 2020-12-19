#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from xmas import Decoder

TESTING = not True
FILENAME = 'sample' if TESTING else 'input'
SIZE = 5 if TESTING else 25


def main():
    stream = read_input(FILENAME)
    dec = Decoder(size=SIZE)
    dec.load_preamble(stream)
    for next_value in stream:
        if dec.is_valid(next_value):
            dec.append(next_value)
        else:
            print(f'Solution 1 is {next_value}')
            break


if __name__ == "__main__":
    main()
