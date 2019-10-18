import math
from PIL import Image

coords_n_shit = {}

with open("elevation_small.txt") as text_file:
    text_contents = text_file.read()
elevations = [[int(each) for each in line.split()]
              for line in text_contents.split("\n")]

# print(elevations[0:100])

map_height = (len(elevations))
# print("map_height = ", map_height)
map_width = (len(elevations[0]))
# print("map_width = ", map_width)

min = int(elevations[0][0])
max = int(elevations[0][0])
print("hi")

for each in elevations:
    for integer in each:
        if int(integer) < min:
            min = int(integer)
        if int(integer) > max:
            max = int(integer)


# print(len(elevations))

for y in range(len(elevations)):
    for x in range(len(elevations)):
        coords_n_shit[(x, y)] = (
            ((int(elevations[y][x])) - min) / (max - min)) * 255
print(coords_n_shit[0])

# colors_big_list = []
# little_rows_of_colors = []

# for rows in elevations:
#     for number in rows:
#         color_int = round(((number - min) / (max-min)) * 255)
#         little_rows_of_colors.append(color_int)
# colors_big_list.append(little_rows_of_colors)
# little_rows_of_colors = []


# image = Image.new('RGB', (map_width, map_height), 'black')
# image.save('pathfinder.png')
# px = image.load()
# # image.putpixel((300, 300), 255)
# px[4, 4] = (255, 255, 255)
# print("pixel")


# def get_coords(number):
#     y = elevation.\
#     x = column[number]
