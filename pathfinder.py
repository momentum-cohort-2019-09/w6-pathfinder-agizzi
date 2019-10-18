import math
from PIL import Image


class Map:
    def __init__(self, file):
        self.file = file

    def read_file(self, file):
        with open(file) as text_file:
            text_contents = text_file.read()

        elevations = [[int(each) for each in line.split()]
                      for line in text_contents.split("\n")]

        min = elevations[0][0]
        max = elevations[0][0]
        print("hi")

        for each in elevations:
            for integer in each:
                if integer < min:
                    min = integer
                if integer > max:
                    max = integer

        colors_big_list = []
        little_rows_of_colors = []

        for rows in elevations:
            for number in rows:
                color_int = round(((number - min) / (max-min)) * 255)
                little_rows_of_colors.append(color_int)
        colors_big_list.append(little_rows_of_colors)
        little_rows_of_colors = []

    def create_map_image(self):
        image = Image.new('RGB', (600, 600), 'black')
        image.save('pathfinder.png')


if __name__ == "__main__":
    map = Map("elevation_small.txt")
