#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from loader import read_input
from jolts import next_options, alternative_paths


def find_path(stack, devices):
    num_sols = 0
    initial_solution = [devices[0]]
    stack.append(initial_solution)
    while stack:
        solution = stack.pop()
        if solution[-1] == devices[-1]:
            num_sols += 1
            print(f"Encontrada sol. {num_sols}: {solution}")
        options = next_options(devices, solution[-1])
        for option in options:
            new_sol = solution[:] + [option]
            stack.append(new_sol)


def main():
    devices = sorted(list(read_input('input')))
    current = 0
    count = 0
    factors = []
    devices.append(devices[-1]+3)
    for device in devices:
        print(f"{current} -> {device}", end=" ")
        delta = device - current
        if delta == 1:
            count += 1
            print(f"[{delta}]")
        else:
            print(f"\u001b[1m\u001b[32m[{delta}]\u001b[0m count is {count}", end="|")
            print(f"count is {count} -> alternatives {alternative_paths(count)}")
            if count >= 2:
                factors.append(alternative_paths(count))
            count = 0
        current = device
    print(f"factors is {factors}")
    sol = functools.reduce(lambda a, b: a*b, factors)
    print(f"Solution is {sol}")


if __name__ == "__main__":
    main()
    


