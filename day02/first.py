import re

class Rule:

    pat = re.compile("(\d+)-(\d+) ([a-z]): (.+)", re.IGNORECASE)

    def __init__(self, line):
        m = self.pat.match(line)
        if m:
            self.min_value = int(m.group(1))
            self.max_value = int(m.group(2))
            self.char = m.group(3)
            self.line = m.group(4)
        else:
            raise ValueError(f"Rule does not match: {line}")

    def is_valid(self):
        n = self.line.count(self.char)
        return self.min_value <= n <= self.max_value



rules = []
with open("input", "r") as f:
    for line in f:
        rule = Rule(line)
        rules.append(rule)

print("Solution:", sum([1 if rule.is_valid() else 0 for rule in rules]))
