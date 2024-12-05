DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
]

def count_xmas(x, y):
    count = 0
    for dx, dy in DIRECTIONS:
        if all(
            0 <= x + i * dx < width and
            0 <= y + i * dy < height and
            words[x + i * dx][y + i * dy] == letter
            for i, letter in enumerate("MAS", start=1)
        ):
            count += 1
    return count


def main():
    result = 0
    for x in range(width):
        for y in range(height):
            if words[x][y] == 'X':
                result += count_xmas(x, y)

    print(f'{result=}')


with open("04_input.txt", "r") as f:
    words = [list(c) for c in [line.strip() for line in f.readlines()]]

width = len(words[0])
height = len(words)
main()