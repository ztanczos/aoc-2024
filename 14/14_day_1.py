import re
from functools import reduce
from operator import mul

result = 0
width = 101
height = 103
duration = 100
robots = []
with open("14_input.txt", "r") as f:
    for line in f:
        px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))

        for sec in range(duration):
            px = (px + vx) % width
            py = (py + vy) % height

        robots.append((px, py))

q_width = width // 2
q_height = height // 2

quadrants = {0: 0, 1: 0, 2: 0, 3: 0}

for robot in robots:
    if robot[0] < q_width:
        if robot[1] < q_height:
            quadrants[0] += 1
        elif robot[1] > q_height:
            quadrants[1] += 1
    elif robot[0] > q_width:
        if robot[1] < q_height:
            quadrants[2] += 1
        elif robot[1] > q_height:
            quadrants[3] += 1

print(reduce(mul, quadrants.values()))
