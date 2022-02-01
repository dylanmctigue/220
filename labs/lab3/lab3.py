"""
Name: Dylan McTigue
lab3.py

Problem: The DOT needs me to help them analyze traffic by writing a program that will
calculate the average number of vehicles that travel each road each day and the overall
total number and average number of vehicles traveled over all of the roads.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():

    acc_total_sum = 0

    roads_surveyed = eval(input("How many roads were surveyed?"))
    for road in range(roads_surveyed):

        acc_sum_per_day = 0

        print("How many days was Road", road + 1, "surveyed?")
        days_surveyed = eval(input(""))

        for day in range(days_surveyed):
            print("How many cars traveled on day", day + 1, "?")
            cars_traveled = eval(input(""))

            acc_total_sum = acc_total_sum + cars_traveled
            acc_sum_per_day = acc_sum_per_day + cars_traveled

        average = acc_sum_per_day / days_surveyed
        print("Road", road + 1, "average vehicles per day: ", average)

    total_avg_per_road = acc_total_sum / roads_surveyed

    print("Total number of vehicles traveled on all roads: ", acc_total_sum)
    print("Average number of vehicles per road: ", total_avg_per_road)

traffic()