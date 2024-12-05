rules = []
with open("05_input.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        rules.append([int(i) for i in line.strip().split('|')])

    result = 0
    for line in f:
        updates = [int(i) for i in line.strip().split(',')]
        for u, update in enumerate(updates):
            for rule in rules:
                if rule[0] == update:
                    if rule[1] in updates and updates.index(rule[1]) <= u:
                        break
            else:
                continue
            break
        else:
            result += updates[(len(updates) // 2)]

print(result)
