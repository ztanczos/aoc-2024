DIRECTIONS = [
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0)  # left
]

with open("06_input.txt", "r") as f:
    layout = [list(line.strip()) for line in f.readlines()]

width = len(layout[0])
height = len(layout)

def traverse(x, y, idx):
    d = DIRECTIONS[idx]
    v = set()
    while True:
        if (x, y, idx) in v:
            return True

        v.add((x, y, idx))

        if 0 <= y + d[1] < height and 0 <= x + d[0] < width:
            if layout[y + d[1]][x + d[0]] == '#':
                idx = (idx + 1) % 4
                d = DIRECTIONS[idx]
            else:
                x += d[0]
                y += d[1]

                if x > width or x < 0 or y > height or y < 0:
                    return False
        else:
            return False


def main():
    result = set()
    guard = {"x": 0, "y": 0}
    i = 0
    d = DIRECTIONS[i]
    sx = 0
    sy = 0
    for y, line in enumerate(layout):
        if '^' in line:
            sx = guard["x"] = line.index('^')
            sy = guard["y"] = y

    while True:
        if 0 <= guard["y"] + d[1] < height and 0 <= guard["x"] + d[0] < width:
            if layout[guard["y"] + d[1]][guard["x"] + d[0]] == '#':
                i = (i + 1) % 4
                d = DIRECTIONS[i]
            else:
                layout[guard["y"] + d[1]][guard["x"] + d[0]] = '#'
                if traverse(sx, sy, 0):
                    result.add((guard["y"] + d[1], guard["x"] + d[0]))

                layout[guard["y"] + d[1]][guard["x"] + d[0]] = '.'
                guard["x"] += d[0]
                guard["y"] += d[1]
        else:
            break

    print(f'{len(result)}')


if __name__ == '__main__':
    main()