import itertools

with open("input", "r") as f:
    numbers = [int(x.strip()) for x in f.readlines() if x]

for a, b in itertools.permutations(numbers, 2):
    if a + b == 2020:
        print(f"Solution: {a}*{b} = {a*b}")
