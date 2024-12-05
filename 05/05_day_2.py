import math
from functools import cmp_to_key


def compare(item1, item2):
    for r in rules:
        if (item1, item2) == (r[0], r[1]):
            return -1
        if (item2, item1) == (r[0], r[1]):
            return 1
    return 0


rules = []
with open("05_input.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        rules.append([int(i) for i in line.strip().split('|')])

    result = 0
    for line in f:
        updates = [int(i) for i in line.strip().split(',')]
        for u, update in enumerate(updates):
            for rule in rules:
                if rule[0] == update:
                    if rule[1] in updates and updates.index(rule[1]) <= u:
                        updates = sorted(updates, key=cmp_to_key(compare))
                        result += updates[((len(updates) - 1) // 2)]
                        break
            else:
                continue
            break

print(result)
