def blink(stones):
    change = []
    for stone in stones:
        if stone == 0:
            change.append(1)
        else:
            num_digits = len(str(stone))
            if num_digits % 2 == 0:
                divisor = 10 ** (num_digits // 2)
                change.append(stone // divisor)
                change.append(stone % divisor)
            else:
                change.append(stone*2024)
    return change


def main():
    with open("11_input.txt", "r") as f:
        stones = list(map(int, f.readline().strip().split()))

    iterations = 25
    for i in range(iterations):
        stones = blink(stones)

    print(len(stones))


if __name__ == "__main__":
    main()