#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from karte import Karte


def first_rule(cell):
    # If a seat is empty (L) and there are no occupied seats adjacent to it,
    # the seat becomes occupied.
    assert cell.is_empty(), "First rule applies only in empty cells"
    if all(not nb.is_occupied() for nb in cell.neighbours()):
        return '#', 1
    return cell.char, 0


def second_rule(cell):
    # If a seat is occupied (#) and four or more seats adjacent to it are also
    # occupied, the seat becomes empty.
    assert cell.is_occupied(),  "Second rule applies only in empty cells"
    if sum(1 if nb.is_occupied() else 0 for nb in cell.neighbours()) >= 4:
        return 'L', 1
    return cell.char, 0
    

def evolve(karte):
    changes = 0
    new_karte = Karte()
    for cell in karte:
        pos = (cell.x, cell.y)
        if cell.char == 'L':
            new_karte[pos], modified = first_rule(cell)
            changes += modified
        elif cell.char == '#':
            new_karte[pos], modified = second_rule(cell)
            changes += modified
        else:
            new_karte[pos] = cell.char
    return new_karte, changes


def main():
    karte = read_input('input')
    round_num = 0
    while True:
        karte, changes = evolve(karte)
        round_num += 1
        if changes == 0:
            break
    print(f"Found stable position in round_num {round_num}")
    sol = sum([
        1 if c.is_occupied() else 0
        for c in karte
        ])
    print(f"Solution 1 is {sol}")


if __name__ == "__main__":
    main()
