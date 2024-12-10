
def defrag():
    left = 0
    right = len(layout) - 1
    while left < right:
        while left < right and layout[right] == '.':
            right -= 1
        while left < right and layout[left] != '.':
            left += 1

        if left < right:
            layout[left], layout[right] = layout[right], layout[left]

def checksum() -> int:
    return sum([pos * id for pos, id in enumerate(layout) if id != '.'])

result = 0
with open("09_input.txt", "r") as f:
    disk = list(map(int, f.readline().strip()))

layout = []
fileId = 0
isFile = True
for d in disk:
    if isFile:
        layout.extend([fileId] * d)
        fileId += 1
    else:
        layout.extend(['.'] * d)
    isFile = not isFile

defrag()
print(checksum())