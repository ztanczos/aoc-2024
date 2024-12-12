
def visit(x, y, visited):
    area = 1
    visited.add((x, y))

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if ((x + dx, y + dy) not in visited and 0 <= x + dx < width
                and 0 <= y + dy < height and garden[y][x] == garden[y + dy][x + dx]):
            d_area, _ = visit(x + dx, y + dy, visited)
            area += d_area

    return area, visited

def perimeter(plot):
    min_x = min(plot, key=lambda p: p[0])[0]
    min_y = min(plot, key=lambda p: p[1])[1]
    max_x = max(plot, key=lambda p: p[0])[0]
    max_y = max(plot, key=lambda p: p[1])[1]

    perim = 0
    for ray_x in range(min_x , max_x + 1):
        is_in = False
        side_count = 0
        for ray_y in range(min_y, max_y + 2):
            if (not is_in and (ray_x, ray_y) in plot) or (is_in and (ray_x, ray_y) not in plot):
                is_in = not is_in
                side_count += 1

        perim += side_count

    for ray_y in range(min_y , max_y + 1):
        is_in = False
        side_count = 0
        for ray_x in range(min_x, max_x + 2):
            if (not is_in and (ray_x, ray_y) in plot) or (is_in and (ray_x, ray_y) not in plot):
                is_in = not is_in
                side_count += 1

        perim += side_count
    return perim

def main():
    visited = set()
    result = 0
    for y, row in enumerate(garden):
        for x, column in enumerate(row):
            if (x, y) not in visited:
                area, v = visit(x, y, set())
                perim = perimeter(v)
                visited.update(v)
                result += area * perim

    print(result)


with open("12_input.txt", "r") as f:
    garden = [line.strip() for line in f.readlines()]

width = len(garden[0])
height = len(garden)

if __name__ == '__main__':
    main()
