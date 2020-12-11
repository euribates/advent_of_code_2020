#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseAnswer:

    def __init__(self):
        self.kernel = set([])

    def __repr__(self):
        buff = ''.join([str(_) for _ in sorted(self.kernel)])
        return f"Answer('{buff}')"

    def __eq__(self, other):
        return self.kernel == other

    def __len__(self):
        return len(self.kernel)


class AnyAnswer(BaseAnswer):
    def __init__(self, items):
        super().__init__()
        for line in items:
            self.kernel |= set(line)


class AllAnswer(BaseAnswer):
    def __init__(self, items):
        super().__init__()
        if items:
            self.kernel = set(items[0])
            for line in items[1:]:
                self.kernel = self.kernel.intersection(set(line))

