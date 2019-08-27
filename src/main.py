import os
import time

from grid import Grid
from utils import config_file

MAX_LOOP = 500
MAX_DIM = 200


def loop(grid):
    grid.visualize()

    while True:
        choice = input("Choose [single, multiple, quit]: ")

        if choice not in ['single', 'multiple', 'quit']:
            print("Wrong Input! Try again ...")
            continue

        elif choice == 'quit':
            print("\n")
            break

        elif choice == 'single':
            grid.update()
            grid.visualize()

        elif choice == 'multiple':
            repeat = input("How many times do you want to repeat? ")

            if not repeat.isdigit() or not 0 < int(repeat) < MAX_LOOP:
                print("Wrong Input! Select a number between 0 and 500")
                continue

            repeat = int(repeat)
            for i in range(repeat):
                print("(phase %i)" % (i + 1))
                time.sleep(1)
                grid.update()
                grid.visualize()


def main():
    print("Welcome to the Game of Life!\n@Created by Jihun Hong\n")

    while True:
        # Receive input from user.
        mode = input("Please choose [custom, random, quit]: ")
        mode = mode.lower()

        if mode == "quit":
            print("See you next time! Bye ...")
            break

        # If input not valid, send error.
        if mode not in ['custom', 'random']:
            print("Wrong Input! Try again ...")
            continue

        if mode == "custom":
            print("Welcome to custom mode ...")
            print("** Make sure to put the file in ../data **")
            file = input("Please enter the file name: ")

            file_path = os.path.join("../data", file)
            row, col, val = config_file(file_path)
            if not val:
                print("File error! The grid is not valid ...")
                continue

            grid = Grid(row, col)
            grid.read_file(file_path)

            loop(grid)

        if mode == "random":
            print("Welcome to random mode ...")
            row = input("Enter number of rows: ")
            col = input("Enter number of columns: ")
            pop = input("Enter the population: ")

            if not row.isdigit() or not col.isdigit() or not pop.isdigit()\
                    or not 0 < int(row) < MAX_DIM or not 0 < int(col) < MAX_DIM or not 0 < int(pop) < int(row) * int(col):
                print("Wrong Input! Row and Column must be integer between 0 and 200 ...")
                continue

            grid = Grid(int(row), int(col))
            grid.randomize(int(pop))
            loop(grid)


if __name__ == "__main__":
    main()
