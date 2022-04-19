"""
Name: Dylan McTigue
lab13.py

Problem: Using all that we have learned this year, create a function that solves a real
world problem involving trade alerts or finding signals. Also, explore algorithms further
in algorithms.py.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    open_file = open(filename, 'r')
    read_file = open_file.read()
    read_file = read_file.split(' ')
    count = 0
    for i in read_file:
        count += 1
        if int(i) > 830:
            print("WARNING: TRADING VOLUME EXCEEDS 830 AT {} SECONDS".format(count))
        elif int(i) == 500:
            print('Pay Attention: Trading Volume Equals 500 at {} seconds'.format(count))
    open_file.close()
