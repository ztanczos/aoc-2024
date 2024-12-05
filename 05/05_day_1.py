rules = []
with open("05_input.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        rules.append([int(i) for i in line.strip().split('|')])

    result = 0
    for line in f:
        updates = [int(i) for i in line.strip().split(',')]
        good = True
        for u, update in enumerate(updates):
            for rule in rules:
                if rule[0] == update:
                    if rule[1] in updates and updates.index(rule[1]) <= u:
                        good = False
                        break
            else:
                continue
            break
        if good:
            result += updates[(len(updates) // 2)]

print(result)
