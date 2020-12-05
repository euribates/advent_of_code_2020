import re

class Rule:

    pat = re.compile("(\d+)-(\d+) ([a-z]): (.+)", re.IGNORECASE)

    def __init__(self, line):
        m = self.pat.match(line)
        if m:
            self.min_index = int(m.group(1)) - 1
            self.max_index = int(m.group(2)) - 1
            self.char = m.group(3)
            self.line = m.group(4)
        else:
            raise ValueError(f"Rule does not match: {line}")

    def is_valid(self):
        a = self.line[self.min_index]
        b = self.line[self.max_index]
        return (
            (a == self.char and b != self.char)
         or (a != self.char and b == self.char)
        )


rules = []
with open("input", "r") as f:
    for line in f:
        rule = Rule(line)
        rules.append(rule)

print("Solution:", sum([1 if rule.is_valid() else 0 for rule in rules]))
