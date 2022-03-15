"""
Name: Dylan McTigue
lab8.py

Problem: I need to wirte a program that takes an input file with students and
their grades and weights for each test, that then outputs a file with that data.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    grade_total = 0
    acc_denom = 0

    for line in in_file:
        acc_avg = 0
        total_weight = 0
        average = 0

        colon_split = line.split(":")

        name = colon_split[0]
        numbers = colon_split[1]
        numbers = numbers.lstrip()

        numb_split = numbers.split(" ")

        numb_length = int((len(numb_split) / 2))

        for i in range(numb_length):
            weight_element = numb_split[0 + acc_avg]
            grade_element = numb_split[1 + acc_avg]

            weight = eval(weight_element)
            total_weight = total_weight + weight

            grade = eval(grade_element)

            average = average + (weight * grade)
            acc_avg = acc_avg + 2

        if total_weight > 100:
            print(name + "'s average: Error: The weights are more than 100.", file=out_file)
        elif total_weight < 100:
            print(name + "'s average: Error: The weights are less than 100.", file=out_file)
        else:
            true_avg = average / 100

            grade_total = grade_total + true_avg

            acc_denom = acc_denom + 1

            print(name + "'s average:", '{:.1f}'.format(true_avg), file=out_file)

    class_average = grade_total / acc_denom

    print("Class average:", '{:.1f}'.format(class_average), file=out_file)

    in_file.close()
    out_file.close()

def main():
    weighted_average("grades.txt", "avg.txt")
main()