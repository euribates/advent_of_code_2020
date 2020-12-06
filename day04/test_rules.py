#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import rules

def test_byr():
    assert rules.is_valid_byr('2002')
    assert rules.is_valid_byr('2003') is False


def test_hgt():
    assert rules.is_valid_hgt("60in")
    assert rules.is_valid_hgt("190cm")
    assert rules.is_valid_hgt("190in") is False
    assert rules.is_valid_hgt("190") is False


def test_hcl():
    assert rules.is_valid_hcl("#123abc")
    assert rules.is_valid_hcl("#123abz") is False
    assert rules.is_valid_hcl("123abc") is False


def test_ecl():
    assert rules.is_valid_ecl("brn")
    assert rules.is_valid_ecl("wat") is False


def test_pid():
    assert rules.is_valid_pid("000000001")
    assert rules.is_valid_pid("0123456789") is False


if __name__ == "__main__":
    pytest.main()
