result = 0
with open("06_input.txt", "r") as f:
    layout = [line.strip() for line in f.readlines()]

width = len(layout[0])
height = len(layout)
visited = set()

DIRECTIONS = [
    (0, -1),    # up
    (1, 0),     # right
    (0, 1),     # down
    (-1, 0)     # left
]

guard = {"x": 0, "y": 0}
i = 0
direction = DIRECTIONS[i]
for y, line in enumerate(layout):
    if '^' in line:
        guard["x"] = line.index('^')
        guard["y"] = y

while True:
    if (guard["x"], guard["y"]) not in visited:
        visited.add((guard["x"], guard["y"]))

    if 0 <= guard["y"] + direction[1] < height and 0 <= guard["x"] + direction[0] < width:
        if layout[guard["y"] + direction[1]][guard["x"] + direction[0]] == '#':
            i = (i + 1) % 4
            direction = DIRECTIONS[i]
        else:
            guard["x"] += direction[0]
            guard["y"] += direction[1]
    else:
        break


print(f'result: {len(visited)}')