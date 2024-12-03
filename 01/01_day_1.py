with open("01_input.txt", "r") as f:
    pairs = [line.strip().split() for line in f]

left_list = [int(left) for left, _ in pairs]
right_list = [int(right) for _, right in pairs]
left_list.sort(), right_list.sort()

distance = sum(abs(left-right) for left, right in zip(left_list, right_list))

print(distance)
