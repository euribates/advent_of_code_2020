#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from xmas import Decoder

TESTING = False
FILENAME = 'sample' if TESTING else 'input'
SIZE = 5 if TESTING else 25


def main():
    all_numbers = list(read_input(FILENAME))
    dec = Decoder(size=SIZE, preamble=all_numbers[0:SIZE])
    invalid_number = None
    for next_value in all_numbers[SIZE:]:
        if dec.is_valid(next_value):
            dec.append(next_value)
        else:
            invalid_number = next_value
            break
    for initial, value in enumerate(all_numbers):
        # print(f"[{initial}: {value}]", end="")
        if value == invalid_number:
            # print('Skipped trivial solution')
            continue
        acc = value
        final = initial + 1
        while final < len(all_numbers) and acc < invalid_number:
            acc += all_numbers[final]
            final += 1
        if acc == invalid_number:
            break
    sequence = all_numbers[initial:final]
    expr = '+'.join(map(str, sequence))
    print(f'Found in positions [{initial}-{final}] {expr} = {invalid_number}')
    print(f"Min value is {min(sequence)}")
    print(f"Max value is {max(sequence)}")
    print(f"Solution 2 is {min(sequence)+max(sequence)}")


if __name__ == "__main__":
    main()
