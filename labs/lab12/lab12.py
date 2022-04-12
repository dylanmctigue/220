"""
Name: Dylan McTigue
lab12.py

Problem: Without using for loops and without using break, develop while control
structures, use Python's built-in list methods, and perform linear search on data
to create functions that help create a game where the user has to guess a random number.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if value == list[i]:
            list.remove(list[i])
            list.insert(i, 'Dylan')
            i = len(list)

        i += 1


def good_input():
    num = eval(input('Input a number from the range of 1-10: '))
    while not 1 <= num <= 10:
        if num < 1:
            num = eval(input('That number was too low. Input a number from the range of 1-10: '))
        if num > 10:
            num = eval(input('That number was too high. Input a number from the range of 1-10: '))
    return num


def num_digits():
    pos_int = True
    while pos_int:
        num = eval(input('Enter a positive integer (Enter a 0 or a negative number to stop): '))
        if num > 0:
            pos_int = True
            count = 0
            check = num
            while check != 0:
                check = check // 10
                count += 1
            print('The number you entered has {} digits'.format(count))
        else:
            pos_int = False


def hi_lo_game():
    rand_num = randint(0, 100)
    i = 0

    while i < 7:
        user_input = eval(input('Guess a number between 1 and 100: '))
        if user_input < rand_num:
            print('That number was too low')
        if user_input > rand_num:
            print('That number was too high')
        if user_input == rand_num:
            print('Correct!')
            print('You win in {} guesses!'.format(i + 1))
            i = 8
        i += 1
    if i == 7:
        print('Sorry, you lose. The number was {}'.format(rand_num))
