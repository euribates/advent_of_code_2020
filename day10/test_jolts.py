#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import jolts


def test_device_jolts():
    assert jolts.device_jolts({3, 9, 6}) == 12


def test_jotls_reduce():
    d = jolts.jolts_reduce([3, 9, 6])
    assert len(d) == 1
    assert d[3] == 4


def test_jotls_reduce_simple():
    from loader import read_input
    devices = list(read_input('simple'))
    stats = jolts.jolts_reduce(devices)
    assert len(stats) == 2
    assert stats[1] == 7
    assert stats[3] == 5


def test_jotls_reduce_sample():
    from loader import read_input
    devices = list(read_input('sample'))
    stats = jolts.jolts_reduce(devices)
    assert len(stats) == 2
    assert stats[1] == 22 
    assert stats[3] == 10


# Second part

def test_next_options():
    assert jolts.next_options([1, 2, 3, 4, 7], 0) == [1, 2, 3]
    assert jolts.next_options([1, 2, 3, 4, 7], 1) == [2, 3, 4]
    assert jolts.next_options([1, 2, 3, 4, 7], 2) == [3, 4, 7]
    assert jolts.next_options([1, 2, 3, 4, 7], 3) == [4, 7]
    assert jolts.next_options([1, 2, 3, 4, 7], 4) == [7]
    assert jolts.next_options([1, 2, 3, 4, 7], 7) == []


def test_alternative_paths():
    assert jolts.alternative_paths(0) == 1
    assert jolts.alternative_paths(1) == 1
    assert jolts.alternative_paths(2) == 2
    assert jolts.alternative_paths(3) == 4
    assert jolts.alternative_paths(4) == 7
    assert jolts.alternative_paths(5) == 13
    assert jolts.alternative_paths(6) == 24
    assert jolts.alternative_paths(7) == 44
    assert jolts.alternative_paths(8) == 81
    assert jolts.alternative_paths(9) == 149


if __name__ == "__main__":
    pytest.main()

