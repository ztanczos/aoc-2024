import itertools


def find_all_c(c):
    coords = set()
    for y in range(height):
        for x in range(width):
            if layout[y][x] == c:
                coords.add((x, y))

    return coords

def find_antinodes(coordinates):
    antinodes = set()
    for (x1, y1), (x2, y2) in itertools.combinations(coordinates, 2):
        dx, dy = x1 - x2, y1 - y2

        for x, y in [(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)]:
            if 0 <= x < width and 0 <= y < height:
                antinodes.add((x, y))

    return antinodes

def main():
    visited = set()
    antinodes = set()

    for y, row in enumerate(layout):
        for x, col in enumerate(row):
            if col != "." and col not in visited:
                coords = find_all_c(col)
                antinodes.update(find_antinodes(coords))
                visited.add(col)
    print(f'result: {len(antinodes)}')


result = 0
layout = []
with open("08_input.txt", "r") as f:
    layout = [list(line.strip()) for line in f.readlines()]

width = len(layout[0])
height = len(layout)

if __name__ == "__main__":
    main()