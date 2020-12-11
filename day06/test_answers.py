#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import answers


def test_create_and_answer():
    a = answers.AnyAnswer(['abcx', 'abcy', 'abcz'])
    assert a.kernel == set('abcxyz')


def test_create_all_answer():
    assert answers.AllAnswer(['abcx', 'abcy', 'abcz']) == set('abc')
    assert answers.AllAnswer(['ab', 'ac']) == set('a')
    assert answers.AllAnswer(['a', 'a', 'a']) == set('a')
    assert answers.AllAnswer(['b']) == set('b')


def test_eq():
    a = answers.AnyAnswer(['abcx', 'abcy', 'abcz'])
    assert a == set('abcxyz')


def test_len():
    a = answers.AnyAnswer(['abcx', 'abcy', 'abcz'])
    assert len(a) == 6


if __name__ == "__main__":
    pytest.main()
