def visit(cell, x, y):
    if cell == 9:
        return [(x, y)]

    ends = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= y + dy < height and 0 <= x + dx < width:
            if hiking_map[y + dy][x + dx] - cell == 1:
                ends += visit(hiking_map[y + dy][x + dx], x + dx, y + dy)
    return ends

def main():
    result = 0
    for y, row in enumerate(hiking_map):
        for x, cell in enumerate(row):
            if cell == 0:
                result += len(set(visit(cell, x, y)))
    print(result)


with open("10_input.txt", "r") as f:
    hiking_map = [[*map(int, d)] for d in [line.strip() for line in f.readlines()]]

width = len(hiking_map[0])
height = len(hiking_map)

if __name__ == '__main__':
    main()