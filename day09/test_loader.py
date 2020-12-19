#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import loader

def test_read_input():
    assert list(loader.read_input("sample")) == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


if __name__ == "__main__":
    pytest.main()
