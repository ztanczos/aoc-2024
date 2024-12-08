import itertools
import operator
from functools import reduce

result = 0

calibrations = []
with open("07_input.txt", "r") as f:
    for line in f:
        parts = line.strip().split(':')
        equation = (int(parts[0]), [int(part) for part in parts[1].split()])
        calibrations.append(equation)

for target, numbers in calibrations:
    for operations in itertools.product([operator.mul, operator.add], repeat=len(numbers) - 1):
        computed_value = reduce(lambda acc, func_num: func_num[0](acc, func_num[1]), zip(operations, numbers[1:]), numbers[0])
        if computed_value == target:
            result += computed_value
            break

print(f'{result=}')