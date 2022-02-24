"""
Name: Dylan McTigue
hw6.py

Problem: Write functions that work with strings and unicode to encode and
encrypt messages by the user. Also begin work writing functions and
returning variables.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def cash_converter():
    integer = eval(input("enter an integer: "))
    print("That is ${:.2f}".format(integer))


def encode():
    message = input("enter a message: ")

    key = eval(input("enter a key: "))

    output = ""

    for i in message:
        message_num = ord(i)
        sum_num = message_num + key
        character = chr(sum_num)
        output = output + character
    print(output)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    acc_sum = 0
    for i in range(number):
        acc_sum = acc_sum + (i + 1)
    return acc_sum


def sum_n_cubes(number):
    acc_sum = 0
    for i in range(number):
        acc_sum = acc_sum + ((i + 1) ** 3)
    return acc_sum


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")

    message_length = len(message)
    key_length = len(key)

    concatenation = ""

    for i in range(message_length):

        each_letter_message = message[i]
        each_letter_key = key[i % key_length]

        message_num = ord(each_letter_message)
        message_new_num = message_num - 65

        keyword_num = ord(each_letter_key)
        keyword_new_num = keyword_num - 65

        sum_num = (message_new_num + keyword_new_num) % 58

        character = chr(sum_num + 65)

        concatenation = concatenation + character

    print(concatenation)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
