#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

import pytest

import xmas


def test_decoder_creation():
    dec = xmas.Decoder(size=5)
    dec.load_preamble(range(5))
    assert len(dec.items) == 5
    assert list(dec.items) == [0, 1, 2, 3, 4]
    print(dec)


def test_decoder_possible_next_values():
    dec = xmas.Decoder(size=5)
    dec.load_preamble(range(5))
    assert dec.possible_next_values() == set([1, 2, 3, 4, 5, 6, 7])
    assert 0 not in dec.possible_next_values()
    assert 1 in dec.possible_next_values()
    assert 2 in dec.possible_next_values()
    assert 3 in dec.possible_next_values()
    assert 4 in dec.possible_next_values()
    assert 5 in dec.possible_next_values()
    assert 6 in dec.possible_next_values()
    assert 7 in dec.possible_next_values()
    assert 8 not in dec.possible_next_values()
    dec = xmas.Decoder(size=5)
    dec.load_preamble(range(1, 6))
    assert dec.possible_next_values() == set([3, 4, 5, 6, 7, 8, 9])
    assert 2 not in dec.possible_next_values()
    assert 3 in dec.possible_next_values()
    assert 4 in dec.possible_next_values()
    assert 5 in dec.possible_next_values()
    assert 6 in dec.possible_next_values()
    assert 7 in dec.possible_next_values()
    assert 8 in dec.possible_next_values()
    assert 9 in dec.possible_next_values()
    assert 10 not in dec.possible_next_values()


@pytest.fixture(scope="function")
def dec25():
    dec = xmas.Decoder(size=25)
    preamble = list(range(1, 26))
    random.shuffle(preamble)
    dec.load_preamble(preamble)
    return dec


def test_26(dec25):
    assert 26 in dec25.possible_next_values()


def test_49(dec25):
    assert 49 in dec25.possible_next_values()


def test_50(dec25):
    assert 50 not in dec25.possible_next_values()
    dec25.append(26)
    assert 50 in dec25.possible_next_values()


def test_100(dec25):
    assert 100 not in dec25.possible_next_values()


def test_decoder_after_append():
    preamble = list(range(1, 26))
    random.shuffle(preamble)
    i = preamble.index(20)
    preamble[0], preamble[i] = preamble[i], preamble[0]
    dec = xmas.Decoder(size=25, preamble=preamble)
    dec.append(45)
    assert dec.is_valid(26)
    assert dec.is_valid(64)
    assert dec.is_valid(65) is False
    assert dec.is_valid(66)


if __name__ == "__main__":
    pytest.main()
