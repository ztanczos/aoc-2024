import re
from sympy import solve, symbols

result = 0
with open("13_input.txt", "r") as f:
    for line in f:
        m = re.search(r'X\+(\d+), Y\+(\d+)', line)
        a1 = int(m.group(1))
        a2 = int(m.group(2))

        line = f.readline()
        m = re.search(r'X\+(\d+), Y\+(\d+)', line)
        b1 = int(m.group(1))
        b2 = int(m.group(2))

        line = f.readline()
        m = re.search(r'X=(\d+), Y=(\d+)', line)
        c1 = int(m.group(1)) + 10000000000000
        c2 = int(m.group(2)) + 10000000000000

        # solve the following linear equation system:
        # a1 * x + b1 * y = c1
        # a2 * x + b2 * y = c2
        x, y = symbols('x y', integer=True)
        solution = solve([a1 * x + b1 * y - c1, a2 * x + b2 * y - c2], syms=(x, y))
        if len(solution) > 0:
            result += solution[x]*3 + solution[y]
        _ = f.readline()

print(result)
