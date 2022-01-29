"""
Name: Dylan McTigue
hw2.py

Problem: develop programs that do take user input and output answers
doing arithmetic using math library.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    my_sum = 0
    for i in range(0, upper_bound + 1, 3):
        my_sum = my_sum + i
    print(my_sum)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))

    form_1 = (side_a + side_b + side_c) / 2
    form_2 = form_1 * (form_1 - side_a) * (form_1 - side_b) * (form_1 - side_c)
    area = math.sqrt(form_2)
    print("The area of the triangle is:", area)


def sum_squares():
    lower_range = eval(input("enter lower range: "))
    upper_range = eval(input("enter upper range: "))
    total_sum = 0
    for i in range(lower_range, upper_range + 1):
        total_sum = total_sum + (i * i)
    print("the sum of squares is", total_sum)


def power():
    base = eval(input("enter base: "))
    exponent = eval(input("enter exponent: "))
    answer = 1
    for i in range(exponent):
        answer = answer * base
    print(base, "^", exponent, "=", answer)


if __name__ == '__main__':
    pass
