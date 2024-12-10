def defrag(layout):
    for index in range(len(layout)-1, -1, -1):
        item = layout[index]
        if item["fileId"] == ".":
            continue
        for s in range(0, index):
            if layout[s]["fileId"] == ".":
                if layout[s]["length"] > item["length"]:
                    remaining = layout[s]["length"] - item["length"]
                    layout[index] = layout[s]
                    layout[s] = item
                    layout[index]["length"] = item["length"]
                    layout.insert(s+1, {"fileId": ".", "length": remaining})
                    break
                elif layout[s]["length"] == item["length"]:
                    layout[index] = layout[s]
                    layout[s] = item
                    break


def checksum(layout) -> int:
    result = 0
    index = 0
    for item in layout:
        if item["fileId"] != ".":
            result += sum((index+i) * item["fileId"] for i in range(item["length"]))
        index += item["length"]
    return result

def main():
    with open("09_input.txt", "r") as f:
        disk = list(map(int, f.readline().strip()))

    layout = []
    fileId = 0
    isFile = True
    for d in disk:
        if isFile:
            layout.append({"fileId": fileId, "length": d})
            fileId += 1
        else:
            layout.append({"fileId": ".", "length": d})
        isFile = not isFile

    defrag(layout)
    print(checksum(layout))

if __name__ == "__main__":
    main()