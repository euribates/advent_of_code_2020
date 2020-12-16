#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import bags


def test_equal_bags():
    shiny_gold = bags.Bag('shiny', 'gold')
    bright_white = bags.Bag('bright', 'white')
    assert shiny_gold == bags.Bag('shiny', 'gold')
    assert shiny_gold != bright_white


def test_expand():
    faded_blue = bags.Bag('faded', 'blue')
    dotted_black = bags.Bag('dotted', 'black')
    vibrant_plum = bags.Bag('vibrant', 'plum')
    vibrant_plum.contains = [
        (faded_blue, 5),
        (dotted_black, 6),
        ]
    assert faded_blue in vibrant_plum.expand()
    assert dotted_black in vibrant_plum.expand()
    all_bags = [faded_blue, dotted_black, vibrant_plum]
    query = dotted_black
    acc = 0
    for bag in all_bags:
        if query in bag.expand():
            acc += 1
    assert acc == 1


def test_count():
    faded_blue = bags.Bag('faded', 'blue')
    faded_blue.contains.append(
        (bags.Bag('rust', 'violet'), 7)
        )
    dotted_black = bags.Bag('dotted', 'black')
    vibrant_plum = bags.Bag('vibrant', 'plum')
    vibrant_plum.contains = [
        (faded_blue, 5),
        (dotted_black, 6),
        ]
    assert vibrant_plum.count() == 46

if __name__ == "__main__":
    pytest.main()

