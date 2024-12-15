import re
from PIL import Image

width = 101
height = 103
robots = []
with open("14_input.txt", "r") as f:
    for line in f:
        robots.append([int(_) for _ in re.findall(r"(-?\d+)", line)])

sec = 0
while True:
    sec += 1
    img = Image.new("RGB", (width, height), "black")
    pixels = img.load()

    x_coords = set()
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height
        pixels[robot[0], robot[1]] = (255, 255, 255)

    for y in range(height):
        count = 0
        for x in range(width):
            if pixels[x, y] == (255, 255, 255):
                count += 1
        if count > 30:
            img.save(f'{sec}.bmp')
            print(f'==== {sec=} ====')
            break
