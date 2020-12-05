#!/usr/bin/env python
# -*- coding: utf-8 -*-


from karte import Karte

karte = Karte('input')
last_line = karte.height
slope = (3, 1)
pos = (0, 0)
count = 0
while pos[1] <= last_line:
    c = karte[pos]
    if c == '#':
        count += 1
    pos = (pos[0]+slope[0], pos[1]+slope[1])

print(f"Solution 1: {count}")


        
