#!/usr/bin/env python
# -*- coding: utf-8 -*-

import loader

karte = {}
for seat in loader.read_input("input"):
    karte[seat.seat_id] = seat

min_seat_id = min(karte.keys())
max_seat_id = max(karte.keys())
for i in range(min_seat_id+1, max_seat_id):
    if (i-1) in karte and i not in karte and (i+1) in karte:
        sol = i
        break

print(f"Solution 2 is {sol}")
