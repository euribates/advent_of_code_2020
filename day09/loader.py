#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input(filename='sample'):
    with open(filename, 'r') as stream:
        for line in stream:
            line = line.strip()
            if line:
                yield int(line)
