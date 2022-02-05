"""
Name: Dylan McTigue
hw3.py

Problem: Develop programs that take user input and give output doing arithmetic with loops. Such
programs will find average with grades, keeps track of tip money in a jar being passed around,
calculate square root using newton's method, output a sequence, and compute pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work, but discussed with Mr. Baier.
"""


def average():
    grades_to_enter = eval(input("How many grades will you enter?"))

    acc_grade = 0

    for i in range(grades_to_enter):
        grade = eval(input("enter grade: "))
        acc_grade = acc_grade + grade

    grade_average = acc_grade / grades_to_enter

    print("the average is", grade_average)


def tip_jar():

    acc_tip = 0

    for i in range(5):
        donation = eval(input("How much would you like to donate?"))
        acc_tip = acc_tip + donation

    print("total tips: ", acc_tip)


def newton():
    sqrt_num = eval(input("What number do you want to square root?"))
    improvement = eval(input("How many times should we improve the approximation?"))

    approx = sqrt_num

    for i in range(improvement):
        approx = (approx + (sqrt_num / approx)) / 2

    print("the square root is approximately: ", approx)


def sequence():
    term_num = eval(input("How many terms would you like?"))
    for i in range(1, term_num + 1):
        terms = (i - 1) + (i % 2)
        print(terms, end=" ")


def pi():
    series_num = eval(input("How many terms in the series?"))
    acc_pi = 1
    for i in range(series_num):
        numerator = i + (2 - (i % 2))
        denominator = i + (1 + (i % 2))
        acc_pi = acc_pi * (numerator / denominator)
    pi_estimate = acc_pi * 2
    print("the estimate for pi is:", pi_estimate)


if __name__ == '__main__':
    pass
