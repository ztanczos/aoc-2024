def can_move(x, y, direction):
    while 0 <= x < width and 0 <= y < height:
        x += direction[0]
        y += direction[1]
        if warehouse[y][x] == "#":
            return False
        if warehouse[y][x] == ".":
            return True
    return False

def move_robot(x, y):
    for move in moves:
        if can_move(x, y, move):
            yy = y + move[1]
            xx = x + move[0]
            if warehouse[yy][xx] != ".":
                while warehouse[yy+move[1]][xx+move[0]] != ".":
                    xx += move[0]
                    yy += move[1]

                warehouse[yy+move[1]][xx+move[0]], warehouse[y+move[1]][x+move[0]] = warehouse[y+move[1]][x+move[0]], warehouse[yy+move[1]][xx+move[0]]

            x += move[0]
            y += move[1]


char_map = {"^": (0, -1),
            ">": (1, 0),
            "<": (-1, 0),
            "v": (0, 1)}

warehouse = []
warehouse_done = False
moves = []
robot_x = 0
robot_y = 0
y = 0
with open("15_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            if "@" in line:
                robot_x = line.index("@")
                robot_y = y
            if warehouse_done:
                moves.extend([char_map[c] for c in line])
            else:
                warehouse.append(list(line))
        else:
            warehouse_done = True
        y += 1

width = len(warehouse[0])
height = len(warehouse)
warehouse[robot_y][robot_x] = "."
move_robot(robot_x, robot_y)

result = 0
for y, line in enumerate(warehouse):
    for x, char in enumerate(line):
        if char == "O":
            result += 100 * y + x

print(f'{result=}')