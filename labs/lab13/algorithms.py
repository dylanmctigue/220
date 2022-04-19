"""
Name: Dylan McTigue
algorithms.py

Problem: Add to algorithms.py for lab 13 by adding a selection sorting algorithm and
and that is then used to sort rectangles and their areas.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Rectangle, Point


def read_data(filename):
    read_file = open(filename, 'r')
    file_string = read_file.read()
    file_string = file_string.replace('\n', ' ')
    file_string = file_string.split(" ")

    i = 0
    while i < len(file_string):
        file_string[i] = eval(file_string[i])
        i += 1
    read_file.close()
    return file_string


def is_in_linear(search_val, values):
    i = 0
    check = False
    while i < len(values):
        if search_val == values[i]:
            check = True
            i = len(values)
        i += 1
    return check


def selection_sort(values):
    length = len(values)

    for unsort_start in range(length - 1):
        acc = unsort_start

        for i in range(unsort_start + 1, length):
            if values[i] < values[acc]:
                acc = i

        values[unsort_start], values[acc] = values[acc], values[unsort_start]


def calc_area(rect):
    rec_one = rect.getP1()
    rec_two = rect.getP2()

    rec_one_x = rec_one.getX()
    rec_two_x = rec_two.getX()
    rec_one_y = rec_one.getY()
    rec_two_y = rec_two.getY()

    width = abs(rec_two_x - rec_one_x)
    length = abs(rec_two_y - rec_one_y)

    area = width * length

    return area


def rect_sort(rectangles):
    length = len(rectangles)

    for unsort_start in range(length - 1):
        acc = unsort_start

        for i in range(unsort_start + 1, length):
            if calc_area(rectangles[i]) < calc_area(rectangles[acc]):
                acc = i

        rectangles[unsort_start], rectangles[acc] = rectangles[acc], rectangles[unsort_start]

    return rectangles
