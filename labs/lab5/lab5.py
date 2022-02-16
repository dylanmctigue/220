"""
Name: Dylan McTigue
lab5.py

Problem: Use python Graphics and strings to create a program that draws a triangle,
one that changes a shapes color, one that manipulates strings, one that manipulates
lists, and one that outputs a series of 2, 4, 6, 2, 4, 6, ....

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Point, GraphWin, Circle, Text, Polygon, Entry, color_rgb
import math

def triange():
    win = GraphWin("Triangle", 500, 500)
    win.setCoords(0, 0, 10, 10)

    point1 = win.getMouse()
    point1.draw(win)
    p1_x = point1.getX()
    p1_y = point1.getY()

    point2 = win.getMouse()
    point2.draw(win)
    p2_x = point2.getX()
    p2_y = point2.getY()

    point3 = win.getMouse()
    point3.draw(win)
    p3_x = point3.getX()
    p3_y = point3.getY()

    line_1_x = (p1_x - p2_x) ** 2
    line_1_y = (p1_y - p2_y) ** 2
    line_1 = math.sqrt(line_1_x + line_1_y)

    line_2_x = (p2_x - p3_x) ** 2
    line_2_y = (p2_y - p3_y) ** 2
    line_2 = math.sqrt(line_2_x + line_2_y)

    line_3_x = (p3_x - p1_x) ** 2
    line_3_y = (p3_y - p1_y) ** 2
    line_3 = math.sqrt(line_3_x + line_3_y)

    triangle = Polygon(point1, point2, point3)
    triangle.setFill("green")
    triangle.draw(win)

    perimeter = line_1 + line_2 + line_3
    perimeter_text = Text(Point(6, 1), "")
    perimeter_text.draw(win)
    perimeter_text.setText(perimeter)

    p_text = Text(Point(4, 1), "Perimeter: ")
    p_text.draw(win)

    s_area = (line_1 + line_2 + line_3) / 2
    area = math.sqrt(s_area * (s_area - line_1) * (s_area - line_2) * (s_area - line_3))
    area_text = Text(Point(6, .5), "")
    area_text.draw(win)
    area_text.setText(area)

    a_text = Text(Point(4, .5), "Area: ")
    a_text.draw(win)

    click_to_close = Text(Point(5, 5), "Click again to close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    red_entry_pt = red_text_pt.clone()
    red_entry_pt.move(50, 0)
    red_entry = Entry(red_entry_pt, 5)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    green_entry_pt = green_text_pt.clone()
    green_entry_pt.move(50, 0)
    green_entry = Entry(green_entry_pt, 5)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    blue_entry_pt = blue_text_pt.clone()
    blue_entry_pt.move(50, 0)
    blue_entry = Entry(blue_entry_pt, 5)

    # display rgb text
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)

    for _ in range(5):
        win.getMouse()

        red_amt = eval(red_entry.getText())
        green_amt = eval(green_entry.getText())
        blue_amt = eval(blue_entry.getText())

        shape.setFill(color_rgb(red_amt, blue_amt, green_amt))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter a string: ")

    first_character = string[0]
    print(first_character)

    last = len(string) - 1
    last_character = string[last]
    print(last_character)

    positions_2_to_5 = string[1:4]
    print(positions_2_to_5)

    concatenation = first_character + last_character
    print(concatenation)

    first_three = string[0:3]
    for _ in range(10):
        print(first_three, end="")

    print()

    for i in range(len(string)):
        each_character = string[i]
        print(each_character)

    num_characters = len(string)
    print(num_characters)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1]
    for _ in range(5):
        print(x, end="")

    print()

    x = values[2:5]
    print(x)

    x = values[2:4] + values[0:1]
    print(x)

    x = values[2:3] + values[0:1] + [eval(values[5])]
    print(x)

    x = values[0] + values[2] + eval(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    terms = eval(input("How many terms would you like to sum? "))

    acc_sum = 0

    for i in range(terms):
        acc_sum = acc_sum + ((i % 3) + 1) * 2
    print("The sum is", acc_sum)


def target():
    win = GraphWin("Target", 500, 500)
    win.setCoords(0, 0, 10, 10)

    circle_1 = Circle(Point(5, 5), 5)
    circle_1.setFill("white")
    circle_1.draw(win)

    circle_2 = Circle(Point(5, 5), 4)
    circle_2.setFill("black")
    circle_2.draw(win)

    circle_3 = Circle(Point(5, 5), 3)
    circle_3.setFill("blue")
    circle_3.draw(win)

    circle_4 = Circle(Point(5, 5), 2)
    circle_4.setFill("red")
    circle_4.draw(win)

    circle_5 = Circle(Point(5, 5), 1)
    circle_5.setFill("yellow")
    circle_5.draw(win)

    click_close = Text(Point(5, 5), "Click again to close")
    click_close.draw(win)
    win.getMouse()
    win.close()