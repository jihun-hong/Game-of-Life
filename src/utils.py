import os


def valid(row, column, i, j):
    return 0 <= i < row and 0 <= j < column


def clean(data):
    return [d.strip("\n") for d in data]


def convert(string):
    if string == "-":
        return 0
    elif string == "+":
        return 1
    raise ValueError("Wrong value!")


def config_path(file):
    path = os.path.join("../data/", file)
    val = os.path.exists(path)
    return path, val


def config_file(path):
    file = open(path, "r")
    data = file.readlines()
    data = clean(data)

    column = len(data[0])
    row = len(data)
    val = True

    for d in data:
        if not column == len(d):
            val = False

    return row, column, val
