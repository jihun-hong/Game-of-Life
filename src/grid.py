import numpy as np
from random import randint

from utils import clean, valid, convert


class Grid(object):
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.grid = np.zeros((row, column), dtype=np.int8)

    def update(self):
        row, column = self.row, self.column
        old_grid = self.grid
        new_grid = np.zeros((row, column), dtype=np.int8)

        for i in range(row):
            for j in range(column):
                count = 0

                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if valid(row, column, i + dx, j + dy):
                            count += old_grid[i + dx][j + dy]

                if count < 2:
                    new_grid[i][j] = 0
                elif count == 2:
                    new_grid[i][j] = old_grid[i][j]
                elif count == 3:
                    new_grid[i][j] = 1
                elif count > 3:
                    new_grid[i][j] = 0

        self.grid = new_grid

    def visualize(self):
        grid, row, column = self.grid, self.row, self.column
        pos, neg, new_line = "+", "-", "\n"

        string = ""
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    string += neg
                else:
                    string += pos
            string += new_line

        print(string)

    def read_file(self, path):
        # Read the data file.
        file = open(path, "r")
        data = file.readlines()
        data = clean(data)

        # Create new grid.
        row, column = self.row, self.column
        new_grid = np.zeros((row, column), dtype=np.int8)

        for i in range(row):
            for j in range(column):
                new_grid[i][j] = convert(data[i][j])

        # Update the grid.
        self.grid = new_grid

    def randomize(self, population):
        used = []
        count = 0
        while True:
            # Select two random integers within index.
            a, b = randint(0, self.row - 1), randint(0, self.column - 1)

            # If not used, fill (a,b) with 1.
            if (a, b) not in used:
                count += 1
                used.append((a, b))
                self.grid[a][b] = 1

            # If population is reached, break.
            if count == population:
                break
