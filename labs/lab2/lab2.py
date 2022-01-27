"""
Name: Dylan McTigue
lab2.py

Problem: Ask the user for a set of numbers, and then find the Root-Mean-Square,
the Harmonic Mean, and the Geometric Mean.
1. The program will ask the user for a set of numbers and then give the user the Root-Mean-Square,
the Harmonic Mean, and the Geometric mean of the numbers given.
2. The inputs is the set numbers given by the user. The outputs are the Root-Mean-Square,
the Harmonic Mean, and the Geometric mean of the numbers given.
3. The program must
    Ask the user for the numbers
    Take the numbers and find the RMS
    Then the Harmonic Mean
    Then the Geometric Mean
    Then tell the user what each one is

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def means():
    values_entered = eval(input("Enter the number of values to be entered: "))

    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1

    for i in range(values_entered):
        value = eval(input("enter value: "))
        rms_acc = rms_acc + (value ** 2)
        harmonic_acc = harmonic_acc + (1 / value)
        geometric_acc = geometric_acc * value

    root_mean_square = round((rms_acc / values_entered) ** 0.5, 3)

    harmonic_mean = round((values_entered / harmonic_acc), 3)

    geometric_mean = round(geometric_acc ** (1 / values_entered), 3)

    print("The Root-Mean-Square is", root_mean_square)
    print("The Harmonic Mean is", harmonic_mean)
    print("The Geometric Mean is", geometric_mean)

means()