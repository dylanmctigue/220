"""
Name: Dylan McTigue
hw1.py

Problem: Writing functions to compute certain scenarios such as the area of the rectangle,
kilometers to miles, and shooting percentage. Allows user to pug in numbers to calculate formulas.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("The area is", area)

def calc_volume():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("The volume of the rectangular solid is", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shoot_percentage = (shots_made / total_shots) * 100
    round_shoot_percentage = round(shoot_percentage, 2)
    print("The shooting percentage is", round_shoot_percentage, "%")

def coffee():
    pounds_coffee_purchase = eval(input("How many pounds of coffee would you like?"))
    total = ((10.50 + .86) * pounds_coffee_purchase) + 1.50
    print("Your total is $", total)

def kilometers_to_miles():
    kilometers_travled = eval(input("How many kilometers did you travel?"))
    k_to_m = kilometers_travled / 1.61
    round_k_to_m = round(k_to_m, 2)
    print("That's", round_k_to_m, "miles!")

if __name__ == '__main__':
    pass
