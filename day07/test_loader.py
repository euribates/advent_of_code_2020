#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import loader


def test_tokenizer():
    tokenizer = loader.Tokenizer("light red bags contain 1 bright white bag, 2 muted yellow bags.\n")
    assert next(tokenizer) == 'light'
    assert next(tokenizer) == 'red'
    assert next(tokenizer) == 'bags'
    assert next(tokenizer) == 'contain'
    assert next(tokenizer) == '1'
    assert next(tokenizer) == 'bright'
    assert next(tokenizer) == 'white'
    assert next(tokenizer) == 'bag,'
    assert next(tokenizer) == '2'
    assert next(tokenizer) == 'muted'
    assert next(tokenizer) == 'yellow'
    assert next(tokenizer) == 'bags.'
    assert next(tokenizer) == '\n'
    
def test_tokenizer_leaf():
    tokenizer = loader.Tokenizer("faded blue bags contain no other bags.\n")
    assert next(tokenizer) == 'faded'
    assert next(tokenizer) == 'blue'
    assert next(tokenizer) == 'bags'
    assert next(tokenizer) == 'contain'
    assert next(tokenizer) == 'no'
    assert next(tokenizer) == 'other'
    assert next(tokenizer) == 'bags.'
    assert next(tokenizer) == '\n'

def test_loader():
    for bag in loader.read_input("sample"):
        print(bag)


if __name__ == "__main__":
    pytest.main()

    
