def pprint(robot_x, robot_y, width, height):
    for y in range(height):
        for x in range(width):
            if (x, y) in walls:
                print("#", end="")
            elif (x, x + 1, y) in boxes:
                print("[]", end="")
            elif (x - 1, x, y) in boxes:
                continue
            elif robot_x == x and robot_y == y:
                print("@", end="")
            else:
                print(".", end="")
        print()

def can_move(x, y, move, width, height, to_move):
    x += move[0]
    y += move[1]
    if x < 0 or x >= width or y < 0 or y >= height:
        return False

    if (x, y) in walls:
        return False

    # horizontal move:
    if move[1] == 0:
        # left move:
        if move[0] == -1:
            if (x + move[0], x, y) in boxes:
                # need to move (x + move[0], x, y) box to left
                to_move.add((x + move[0], x, y))
                return can_move(x + move[0], y, move, width, height, to_move)
        # right move
        else:
            if (x, x + move[0], y) in boxes:
                to_move.add((x, x + move[0], y))
                return can_move(x + move[0], y, move, width, height, to_move)

    # vertical move:
    if move[0] == 0:
        if (x - 1, x, y) in boxes:
            to_move.add((x - 1, x, y))
            return can_move(x - 1, y, move, width, height, to_move) and can_move(x, y, move, width, height, to_move)
        if (x, x + 1, y) in boxes:
            to_move.add((x, x + 1, y))
            return can_move(x, y, move, width, height, to_move) and can_move(x + 1, y, move, width, height, to_move)

    return True

def move_robot(x, y, width, height):
    for move in moves:
        to_move = set()
        if can_move(x, y, move, width, height, to_move):
            for each in to_move:
                boxes.remove(each)
            for each in to_move:
                boxes.add((each[0] + move[0], each[1] + move[0], each[2] + move[1]))
            x += move[0]
            y += move[1]


def main():
    warehouse_done = False
    robot_x = 0
    robot_y = 0
    width = 0
    height = 0
    y = 0
    with open("15_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                if warehouse_done:
                    moves.extend([char_map[c] for c in line])
                else:
                    x = 0
                    for char in line:
                        if char == '#':
                            walls.append((x, y))
                            walls.append((x + 1, y))
                        elif char == "O":
                            boxes.add((x, x + 1, y))
                        elif char == "@":
                            robot_x = x
                            robot_y = y
                        x += 2
                        if x > width:
                            width = x
            else:
                warehouse_done = True
            if not warehouse_done:
                y += 1
                if y > height:
                    height = y


    move_robot(robot_x, robot_y, width, height)
    result = 0
    for box in boxes:
        result += 100 * box[2] + box[0]

    print(result)


char_map = {"^": (0, -1),
            ">": (1, 0),
            "<": (-1, 0),
            "v": (0, 1)}
walls = []
boxes = set()
moves = []

if __name__ == "__main__":
    main()