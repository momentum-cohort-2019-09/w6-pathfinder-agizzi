import math
from PIL import Image
import numpy as np


class Map:
    def __init__(self, file):
        self.file = file
        self.elevations = []
        self.min_elevation = []
        self.max_elevation = []
        self.text_contents = []
        self.colors_big_list = []
        self.little_rows_of_colors = []

    def read_file(self):
        with open(self.file) as text_file:
            self.text_contents = text_file.read()

    def find_elevations(self):
        self.elevations = [[int(each) for each in line.split()]
                           for line in self.text_contents.split("\n")]

    def find_min_and_max(self):
        self.min_elevation = self.elevations[0][0]
        self.max_elevation = self.elevations[0][0]

        for each in self.elevations:
            for integer in each:
                if integer < self.min_elevation:
                    self.min_elevation = integer
                if integer > self.max_elevation:
                    self.max_elevation = integer

    def get_colors_from_elevations(self):
        for rows in self.elevations:
            for number in rows:
                color_int = round(
                    ((number - self.min_elevation) / (self.max_elevation-self.min_elevation)) * 255)
                self.little_rows_of_colors.append(color_int)
            self.colors_big_list.append(self.little_rows_of_colors)
            self.little_rows_of_colors = []
        print("i am running")
        # print(self.colors_big_list)

    def create_map_image(self):
        print("create_map")
        img = Image.fromarray(np.uint8(self.colors_big_list))
        img.save("test.png")


if __name__ == "__main__":
    map = Map("elevation_small.txt")
    map.read_file()
    map.find_elevations()
    map.find_min_and_max()
    map.get_colors_from_elevations()
    map.create_map_image()
