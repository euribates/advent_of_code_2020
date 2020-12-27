#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Cell:

    AXIS = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0)
    ]

    def __init__(self, karte, x, y, char):
        self.karte = karte
        self.x = x
        self.y = y
        self.char = char

    def __str__(self):
        return self.char

    def is_free(self):
        return self.char in {'.', 'L'}

    def is_empty(self):
        return self.char == 'L'

    def is_occupied(self):
        return self.char == '#'

    def is_seat(self):
        return self.char in {'#', 'L'}

    def is_inside_limits(self, x, y):
        return 0 <= x < self.karte.columns and 0 <= y < self.karte.rows

    def neighbours(self):
        for xx in range(self.x-1, self.x+2):
            for yy in range(self.y-1, self.y+2):
                if xx == self.x and yy == self.y:
                    continue
                if self.is_inside_limits(xx, yy):
                    yield self.karte[xx, yy]

    def orthogonal_seats(self):  # For the second part
        result = []
        for dx, dy in self.AXIS:
            x, y = self.x + dx, self.y + dy
            while self.is_inside_limits(x, y):
                cell = self.karte[x, y]
                if cell.is_seat():
                    result.append(cell)
                    break
                x, y = x + dx, y + dy
        return result








class KarteIterator:

    def __init__(self, karte):
        self.karte = karte
        self.x = 0
        self.y = 0

    def __next__(self):
        if self.y == self.karte.rows:
            raise StopIteration
        result = self.karte[(self.x, self.y)]
        self.x += 1
        if self.x == self.karte.columns:
            self.x = 0
            self.y += 1
        return result


class Karte:

    def __init__(self):
        self.kernel = {}
        self.columns = 0
        self.rows = 0

    def __setitem__(self, coords, char):
        x, y = coords
        self.columns = max(self.columns, x+1)
        self.rows = max(self.rows, y+1)
        self.kernel[coords] = Cell(self, x, y, char)

    def __getitem__(self, coords):
        return self.kernel[coords]

    def __iter__(self):
        return KarteIterator(self)

    def __str__(self):
        buff = []
        for i, cell in enumerate(self):
            buff.append(cell.char)
            if (i+1) % self.columns == 0:
                buff.append("\n")
        return "".join(buff)


