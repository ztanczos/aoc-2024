
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

    # vertical rays
    hits = {}
    for ray_x in range(min_x - 1, max_x + 1):
        is_in = False
        hits[ray_x] = []
        for ray_y in range(min_y - 1, max_y + 2):
            if (not is_in and (ray_x, ray_y) in plot) or (is_in and (ray_x, ray_y) not in plot):
                is_in = not is_in
                hits[ray_x].append((ray_y, is_in))

    side_count = 0
    for i, hit_x in enumerate(hits):
        if i > 0:
            for (y, is_in) in hits[hit_x]:
                if (y, is_in) not in hits[hit_x - 1]:
                    side_count += 1

    # horizontal rays
    hits = {}
    for ray_y in range(min_y - 1, max_y + 1):
        is_in = False
        hits[ray_y] = []
        for ray_x in range(min_x - 1, max_x + 2):
            if (not is_in and (ray_x, ray_y) in plot) or (is_in and (ray_x, ray_y) not in plot):
                is_in = not is_in
                hits[ray_y].append((ray_x, is_in))

    for i, hit_y in enumerate(hits):
        if i > 0:
            for (y, is_in) in hits[hit_y]:
                if (y, is_in) not in hits[hit_y - 1]:
                    side_count += 1
    return side_count

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
