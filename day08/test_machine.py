#!/usr/bin/env python
# -*- coding: utf-8 -*-

import machine

import pytest

LINE_SAMPLES = [
    ('nop +0', ('nop', 0)),
    ('acc +1', ('acc', 1)),
    ('jmp +4', ('jmp', 4)),
    ('acc +3', ('acc', 3)),
    ('jmp -3', ('jmp', -3)),
    ('acc -99', ('acc', -99)),
    ('acc +1', ('acc', 1)),
    ('jmp -4', ('jmp', -4)),
    ('acc +6', ('acc', 6)),
]


@pytest.fixture(scope="module", params=LINE_SAMPLES, ids=[_[0] for _ in LINE_SAMPLES])
def line_example(request):
    return request.param


def test_create_with_tuple(line_example):
    line, name_and_value = line_example
    assert machine.OP(line) == machine.OP(name_and_value)


def test_create(line_example):
    line, (code, value) = line_example
    op = machine.OP(line)
    assert op.code == code
    assert op.value == value


def test_acc():
    proc = machine.Proc()
    assert proc.PC == 0
    assert proc.ACC == 0
    acc = machine.OP('acc +7')
    proc.execute(acc)
    assert proc.PC == 1
    assert proc.ACC == 7


def test_nop():
    proc = machine.Proc()
    assert proc.PC == 0
    assert proc.ACC == 0
    nop = machine.OP('nop +0')
    proc.execute(nop)
    assert proc.PC == 1
    assert proc.ACC == 0
    proc.execute(nop)
    assert proc.PC == 2
    assert proc.ACC == 0


def test_jmp():
    proc = machine.Proc()
    assert proc.PC == 0
    assert proc.ACC == 0
    jmp1 = machine.OP('jmp +1')
    proc.execute(jmp1)
    assert proc.PC == 1
    jmp7 = machine.OP('jmp +7')
    proc.execute(jmp7)
    assert proc.PC == 8
    jmp_minus_3 = machine.OP('jmp -3')
    proc.execute(jmp_minus_3)
    assert proc.PC == 5


if __name__ == "__main__":
    pytest.main()
