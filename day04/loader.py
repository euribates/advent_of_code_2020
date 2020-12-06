#!/usr/bin/env python
# -*- coding: utf-8 -*-


def load_passport(stream):
    data = {}
    line = stream.readline().strip()
    while line:
        for par in line.split(' '):
            key, value = par.split(":")
            data[key] = value
        line = stream.readline().strip()
    return data

def read_input(filename="input"):
    with open('input', 'r') as f:
        passport = load_passport(f)
        while passport:
            yield passport
            passport = load_passport(f)
