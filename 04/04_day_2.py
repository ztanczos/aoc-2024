def is_mas(x, y):
    if 0 < x < len(words[0]) - 1 and 0 < y < len(words) - 1:
        if (((words[x - 1][y - 1] == 'M' and words[x + 1][y + 1] == 'S') or (
                words[x - 1][y - 1] == 'S' and words[x + 1][y + 1] == 'M'))
                and ((words[x + 1][y - 1] == 'M' and words[x - 1][y + 1] == 'S') or (
                        words[x + 1][y - 1] == 'S' and words[x - 1][y + 1] == 'M'))):
            return True
    return False


def main():
    result = 0
    for x in range(len(words[0])):
        for y in range(len(words)):
            if words[x][y] == 'A' and is_mas(x, y):
                result += 1

    print(f'{result=}')


with open("04_input.txt", "r") as f:
    words = [list(c) for c in [line.strip() for line in f.readlines()]]

main()