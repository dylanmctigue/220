"""
Name: Dylan McTigue
hw8.py

Problem: Learning and practicing Accumulations and using conditional control structures.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Circle, Point, GraphWin, Text
import math

def add_ten(nums):
    length = len(nums)
    for i in range(length):
        nums[i] = nums[i] + 10


def square_each(nums):
    length = len(nums)
    for i in range(length):
        nums[i] = nums[i] ** 2



def sum_list(nums):
    list_sum = 0
    for i in range(len(nums)):
        list_sum = nums[i] + list_sum
    return list_sum


def to_numbers(nums):
    length = len(nums)
    for i in range(length):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    my_list = []
    for i in range(len(nums)):
        sum_num = 0
        each_element = nums[i].split(", ")
        to_numbers(each_element)
        square_each(each_element)
        new_numb = sum_list(each_element)
        sum_num = sum_num + new_numb
        sum_num_list = [sum_num]
        my_list = my_list + sum_num_list
    return my_list


def starter(weight, wins):
    if (weight >= 150 and weight < 160) and (wins >= 5):
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year / 400 == int(year / 400):
        return True
    elif year / 100 == int(year / 100):
        return False
    elif year / 4 == int(year / 4):
        return True
    else:
        return False



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center_1 = win.getMouse()
    circumference_point_1 = win.getMouse()
    radius_1 = math.sqrt(
        (center_1.getX() - circumference_point_1.getX()) ** 2 + (center_1.getY() - circumference_point_1.getY()) ** 2)
    circle_one = Circle(center_1, radius_1)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        overlap = Text(Point(5, 5), "The Circles Overlap")
        overlap.draw(win)
    else:
        not_overlap = Text(Point(5, 5), "The Circles Do Not Overlap")
        not_overlap.draw(win)

    click_to_close = Text(Point(5, 3), "Click to Close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    circle_one_center = circle_one.getCenter()
    circle_two_center = circle_two.getCenter()

    circle_one_x = circle_one_center.getX()
    circle_one_y = circle_one_center.getY()
    circle_two_x = circle_two_center.getX()
    circle_two_y = circle_two_center.getY()

    diff_x = (circle_two_x - circle_one_x) ** 2
    diff_y = (circle_two_y - circle_one_y) ** 2

    distance = math.sqrt(diff_x + diff_y)

    radius_sum = circle_one.getRadius() + circle_two.getRadius()

    if distance > radius_sum:
        return False
    else:
        return True

circle_overlap()

if __name__ == '__main__':
    pass
