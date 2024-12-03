import re

with open("03_input.txt", "r") as f:
    result = 0
    for line in f:
        memory = line.strip()
        instructions = [v for v in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)]
        result += sum([int(i) * int(j) for i, j in instructions])

    print(result)