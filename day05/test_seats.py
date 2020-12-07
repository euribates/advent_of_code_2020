#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from seats import Seat


KNOWN_VALUES = [
    ("FBFBBFFRLR", (44, 5, 357)),
    ("BFFFBBFRRR", (70, 7, 567)),
    ("FFFBBBFRRR", (14, 7, 119)),
    ("BBFFBBFRLL", (102, 4, 820)),
]


@pytest.fixture(params=KNOWN_VALUES, ids=[_[0] for _ in KNOWN_VALUES])
def known_values(request):
    return request.param


def test_properties(known_values):
    label, values = known_values
    (rows, columns, seat_id) = values
    seat = Seat(label)
    assert seat.row == rows
    assert seat.column == columns
    assert seat.seat_id == seat_id


if __name__ == "__main__":
    pytest.main()
