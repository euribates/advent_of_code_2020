#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

ERROR = "\u001b[31m[ERROR]\u001b[0m"
OK = "\u001b[32m[OK]\u001b[0m"


class OP:

    pat_op = re.compile(r'(acc|jmp|nop) ([+\-]\d+)')

    def __init__(self, line_or_tuple):
        if isinstance(line_or_tuple, tuple):
            self.code, self.value = line_or_tuple
        else:
            m = self.pat_op.match(line_or_tuple)
            self.code = m.group(1)
            self.value = int(m.group(2))

    def __str__(self):
        return f"{self.code} {'+' if self.value >= 0 else ''}{self.value}"

    def __eq__(self, other):
        return self.code == other.code and self.value == other.value


class Proc:

    def __init__(self):
        self.kernel = {
            'acc': self.do_acc,
            'jmp': self.do_jmp,
            'nop': self.do_nop,
        }
        self.memory = []
        self.reset()

    def reset(self):
        self.PC = 0
        self.ACC = 0
        self.visited = set()

    def execute(self, op):
        handler = self.kernel[op.code]
        handler(op)

    def __len__(self):
        return len(self.memory)

    def do_acc(self, op):
        self.ACC += op.value
        self.PC += 1

    def do_jmp(self, op):
        self.PC += op.value

    def do_nop(self, op):
        self.PC += 1

    def load_memory(self, seq_ops):
        self.memory = list(seq_ops)
        self.reset()

    def run(self, trace_on=False):
        next_op = self.memory[self.PC]
        while self.PC not in self.visited:
            if trace_on:
                print(f'[{self.PC}] {next_op}', end=' ')
                print(f"[Visited {self.visited}", end=" -> ")
            self.visited.add(self.PC)
            if trace_on:
                print(f"{self.visited}]", end=" ")
            self.execute(next_op)
            if trace_on:
                print(f' [ACC: {self.ACC}] {OK}')
            if self.PC == len(self.memory):
                break
            next_op = self.memory[self.PC]
        if self.PC in self.visited:
            if trace_on:
                print(ERROR, f'Memory position {self.PC} accesed again')
                print(f"ACC: {self.ACC} PC: {self.PC} Mem. size: {len(self)}")
            return False
        if trace_on:
            print(OK, f'Memory position {self.PC} placed just after program size')
            print(f"ACC: {self.ACC} PC: {self.PC} Mem. size: {len(self)}")
        return True
        
