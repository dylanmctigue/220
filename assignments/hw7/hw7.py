"""
Name: Dylan McTigue
hw7.py

Problem: This assignment has me creating programs to read and write text files.
It will help me learn how to manipulate files through Python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    acc_num = 0

    for line in in_file:
        words = line.split()

        for i in range(len(words)):
            word = words[i]

            acc_num = acc_num + 1

            print(str(acc_num) + " " + word, file=out_file)

    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    for line in in_file:
        elements = line.split()

        first_name = elements[0]
        last_name = elements[1]
        wage = elements[2]
        hours = elements[3]

        product = eval(wage) * eval(hours)
        bonus_product = eval(hours) * 1.65
        total = product + bonus_product

        print(first_name + " " + last_name + " " + str('{:.2f}'.format(total)), file=out_file)


def calc_check_sum(isbn):
    new_isbn = isbn.replace("-", "")

    product = 0
    product_acc = 10

    for num in range(len(new_isbn)):
        product = (eval(new_isbn[num]) * product_acc) + product

        product_acc = product_acc - 1

    return product


def send_message(file_name, friend_name):
    in_file = open(file_name, "r")
    out_file = open(friend_name + ".txt", "w")

    data = in_file.read()

    print(data, file=out_file, end="")

    in_file.close()
    out_file.close()

def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, "r")
    out_file = open(friend_name + ".txt", "w")

    for line in in_file:
        output = encode(line[:-1], key)
        print(output, file=out_file)

    in_file.close()
    out_file.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, "r")
    out_file = open(friend_name + ".txt", "w")
    pad = open(pad_file_name, "r")

    text_data = in_file.read()
    pad_data = pad.read()

    output = encode_better(text_data, pad_data)

    print(output, file=out_file)

    in_file.close()
    out_file.close()


if __name__ == '__main__':
    pass
