"""
Name: Dylan McTigue
algorithms.py

Problem: Without using for loops and without using break, develop while control
structures, use Python's built-in list methods, and perform linear search on data
to create functions that help create a game where the user has to guess a random number.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


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
