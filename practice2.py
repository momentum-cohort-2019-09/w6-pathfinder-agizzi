import math
from PIL import Image
import numpy as np

with open("elevation_small.txt") as text_file:
    text_contents = text_file.read()

elevations = [[int(each) for each in line.split()]
              for line in text_contents.split("\n")]


min_elevation = elevations[0][0]
max_elevation = elevations[0][0]

for each in elevations:
    for integer in each:
        if integer < min_elevation:
            min_elevation = integer
        if integer > max_elevation:
            max_elevation = integer


colors_big_list = []
little_rows_of_colors = []

for rows in elevations:
    for number in rows:
        color_int = round(((number - min_elevation) /
                           (max_elevation-min_elevation)) * 255)
        little_rows_of_colors.append(color_int)
    colors_big_list.append(little_rows_of_colors)
    little_rows_of_colors = []

img = Image.fromarray(np.uint8(colors_big_list))≈

img.save('pathfinder.png')
