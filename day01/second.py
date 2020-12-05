import itertools

with open("input", "r") as f:
    numbers = [int(x.strip()) for x in f.readlines() if x]

for a, b, c in itertools.permutations(numbers, 3):
    if a + b + c == 2020:
        print(f"{a}+{b}+{c} = {a+b+c}")
        print(f"Solution: {a}*{b}*{c} = {a*b*c}")
