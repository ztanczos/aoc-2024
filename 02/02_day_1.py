import math

with open("02_input.txt", "r") as f:
    safe_levels = 0
    for line in f:
        levels = [int(l) for l in line.strip().split()]
        sign = math.copysign(1, levels[1]-levels[0])
        good = True
        for i in range(1,len(levels)):
            diff = levels[i] - levels[i-1]
            if abs(diff) > 3 or abs(diff) < 1 or math.copysign(1, diff) != sign:
                good = False
                break

        if good:
            safe_levels += 1

    print(f'{safe_levels=}')