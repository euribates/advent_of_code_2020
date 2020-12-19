#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loader import read_input
from machine import Proc, OP


def swap_op(op):
    if op.code == 'jmp':
        return OP(('nop', op.value)) 
    elif op.code == 'nop':
        return OP(('jmp', op.value)) 
    else:
        raise ValueError(f'Op. code must be jmp or nop, not {op}')


def main():
    proc = Proc()
    proc.load_memory(read_input('input'))
    for index, op in enumerate(proc.memory):
        if op.code == 'acc':
            continue
        new_op = swap_op(op)
        proc.memory[index] = new_op
        proc.reset()
        success = proc.run()
        if success:
            print(
                f"Solution is to change instruction on index {index}",
                f"from {op} to {new_op}",
                )
            print(f"Solution 2: {proc.ACC}")
            break
        else:  # Restore memory
            proc.memory[index] = op


if __name__ == "__main__":
    main()
