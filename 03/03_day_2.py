import re

with open("03_input.txt", "r") as f:
    result = 0
    enabled = True
    for line in f:
        memory = line.strip()
        instructions = [(m.start(0), [int(m.group(1)), int(m.group(2))]) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', memory)]
        startStop = [(m.start(0), m.group(0)) for m in re.finditer(r'(do\(\)|don\'t\(\))', memory)]
        print(startStop)
        i = 0
        for instruction in instructions:
            if len(startStop) > i and instruction[0] > startStop[i][0]:
                if startStop[i][1] == "don't()":
                    enabled = False
                else:
                    enabled = True
                i += 1

            if enabled:
                result += instruction[1][0] * instruction[1][1]
            print(f'enabled: {enabled}, index: {instruction[0]}: {instruction[1][0]}*{instruction[1][1]}')

    print(result)