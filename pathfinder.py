import math
from PIL import Image
import numpy as np
import random as r


class Map:
    def __init__(self, file):
        self.file = file
        self.elevations = []
        self.min_elevation = []
        self.max_elevation = []
        self.text_contents = []
        self.colors_big_list = []
        self.little_rows_of_colors = []
        self.paths = []
        self.img = ''

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
        self.img = Image.fromarray(np.uint8(self.colors_big_list))
        self.img.save("test.png")

        # print(self.elevations[0])


class Path:
    def __init__(self, elevations, map):
        self.position = 0
        self.elevations = elevations
        self.previous_points = []
        self.map_pixels = ''
        self.path = []
        self.map = map

    def determine_map_pixels(self):
        self.map.img = self.map.img.convert('RGB')
        self.map_pixels = self.map.img.load()

    def draw_path(self, point):
        self.map_pixels[point[1], point[0]] = (255, 0, 0)
        # print(self.map_pixels)
        print(self.map_pixels[1, 1])

    def find_path(self):
        y = r.randint(0, len(self.elevations))
        x = 0
        while x < (len(self.elevations)-1):
            point = []
            NE = abs((self.elevations[y-1][x+1]) - self.position)
            E = abs((self.elevations[y][x+1]) - self.position)
            SE = abs((self.elevations[y+1][x+1]) - self.position)
            smallest_delta = min(NE, E, SE)
            if smallest_delta == NE:
                y -= 1
                x += 1
                point.append(y)
                point.append(x)
                self.position = self.elevations[y][x]
                self.draw_path(point)
            elif smallest_delta == E:
                x += 1
                point.append(y)
                point.append(x)
                self.position = self.elevations[y][x]
                self.draw_path(point)
            else:
                y += 1
                x += 1
                point.append(y)
                point.append(x)
                self.position = self.elevations[y][x]
                self.draw_path(point)
            # print(point)
        # print(x)


if __name__ == "__main__":
    map = Map("elevation_small.txt")
    map.read_file()
    map.find_elevations()
    map.find_min_and_max()
    map.get_colors_from_elevations()
    map.create_map_image()
    path = Path(map.elevations, map)
    path.determine_map_pixels()
    path.find_path()
