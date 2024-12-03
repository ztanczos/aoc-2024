import math

def is_safe(readings):
    s = math.copysign(1, readings[1] - readings[0])
    for x in range(1, len(readings)):
        d = readings[x] - readings[x - 1]
        if abs(d) > 3 or abs(d) < 1 or math.copysign(1, d) != s:
            return False
    return True

with open("02_input.txt", "r") as f:
    safe_levels = 0
    for line in f:
        levels = [int(l) for l in line.strip().split()]
        if is_safe(levels):
            safe_levels += 1
            continue
        else:
            for i in range(1, len(levels)+1):
                if is_safe([x for j,x in enumerate(levels) if j != i-1]):
                    safe_levels += 1
                    break
    print(f'{safe_levels=}')

