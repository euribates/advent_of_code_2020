#!/usr/bin/env python
# -*- coding: utf-8 -*-

import loader

seats = list(loader.read_input("input"))
print("Solution 1 is", max([s.seat_id for s in seats]))
