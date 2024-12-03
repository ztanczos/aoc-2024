from collections import Counter

with open("01_input.txt", "r") as f:
    pairs = [line.strip().split() for line in f]

left_list = [left for left, _ in pairs]
right_list = [right for _, right in pairs]

right_count = Counter(right_list)

similarity = sum(int(left) * right_count[left] for left in left_list)
print(similarity)
