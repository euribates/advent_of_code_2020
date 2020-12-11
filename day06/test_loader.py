#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import loader

def test_read_input():
    results = list(loader.read_input('sample'))
    assert len(results) == 5
    assert results[0] == ['abc']
    assert results[1] == ['a', 'b', 'c']
    assert results[2] == ['ab', 'ac']
    assert results[3] == ['a', 'a', 'a', 'a']
    assert results[4] == ['b']


if __name__ == "__main__":
    pytest.main()
