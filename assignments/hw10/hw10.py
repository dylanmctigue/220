"""
Name: Dylan McTigue
hw10.py

Problem: Create functions that use decision and repetition structures, boolean values,
and create classes and objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(n):
    num_1 = 1
    num_2 = 0
    num_sum = 0
    count = 0
    if n == 1:
        return 1
    if n > 1:
        while count < n:
            num_sum = num_1 + num_2
            num_1 = num_2
            num_2 = num_sum
            count += 1
        return num_sum
    else:
        return None


def double_investment(principle, rate):
    double_principle = principle * 2
    count = 0
    while principle < double_principle:
        principle = principle * (1 + rate)
        count += 1
    return count


def syracuse(n):
    syra_list = [n]
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        syra_list.append(int(n))
    return syra_list


def check_prime(n):
    if n == 1:
        return False
    if n == 0:
        return True
    check = 0
    acc = 2
    while acc <= (n - 1):
        if n % acc == 0:
            check = 1
            break
        acc += 1
    if check == 0:
        return True
    else:
        return False


def goldbach(n):
    if n % 2 != 0:
        return None
    acc = 2
    prime_list = []
    while acc < n:
        if check_prime(acc):
            prime_list = prime_list + [acc]
        acc += 1

    i = 0
    while prime_list[i] <= n:
        diff = n - prime_list[i]
        if diff in prime_list:
            return [prime_list[i], diff]
        i += 1
