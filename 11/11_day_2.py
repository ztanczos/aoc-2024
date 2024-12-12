from collections import Counter

def blink(stones):
    change = Counter()
    for stone in stones:
        count = stones[stone]
        if stone == 0:
            change[1] += count
        else:
            num_digits = len(str(stone))
            if num_digits % 2 == 0:
                divisor = 10 ** (num_digits // 2)
                change[stone // divisor] += count
                change[stone % divisor] += count
            else:
                change[stone*2024] += count
    return change

def main():
    with open("11_input.txt", "r") as f:
        stones = list(map(int, f.readline().strip().split()))

    iterations = 75
    unique_stones = Counter(stones)
    for i in range(iterations):
        unique_stones = blink(unique_stones)

    print(sum(unique_stones.values()))


if __name__ == "__main__":
    main()