"""
Name: Dylan McTigue
hw4.py

Problem: Writing programs using the Python graphics library. Also has practice with
accumulating sequences.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import GraphWin, Point, Text, Rectangle, Circle


def squares():

    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    win.setCoords(0, 0, 10, 10)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    shape = Rectangle(Point(1, 1), Point(2, 2))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape_clone = shape.clone()
        shape_clone.draw(win)
        shape.move(change_x, change_y)

    close = Text(Point(5, 5), "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    win.setCoords(0, 0, 10, 10)

    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_2.draw(win)

    four_side_shape = Rectangle(point_1, point_2)
    four_side_shape.draw(win)
    four_side_shape.setFill("green")

    perimeter = round((abs(point_1.getX() - point_2.getX()) * 2) +
                      (abs(point_1.getY() - point_2.getY()) * 2), 3)
    perimeter_text = Text(Point(5.5, 2), "")
    perimeter_text.draw(win)
    perimeter_text.setText(perimeter)

    p_text = Text(Point(4.5, 2), "Perimeter: ")
    p_text.draw(win)

    area = round((abs(point_1.getX() - point_2.getX())) *
                 (abs(point_1.getY() - point_2.getY())), 3)
    area_text = Text(Point(5.5, 1), "")
    area_text.draw(win)
    area_text.setText(area)

    a_text = Text(Point(4.5, 1), "Area: ")
    a_text.draw(win)

    click_to_close = Text(Point(5, 5), "Click again to close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 500, 500)
    win.setCoords(0, 0, 10, 10)

    click_1 = win.getMouse()
    click_1.draw(win)
    click_2 = win.getMouse()
    click_2.draw(win)

    radius = math.sqrt(((click_1.getX() - click_2.getX()) ** 2) +
                       ((click_1.getY() - click_2.getY()) ** 2))

    circle_shape = Circle(click_1, radius)
    circle_shape.draw(win)
    circle_shape.setFill("light blue")

    radius_text = Text(Point(6, 1), "")
    radius_text.draw(win)
    radius_text.setText(radius)
    r_text = Text(Point(4, 1), "Radius:")
    r_text.draw(win)

    close_win = Text(Point(5, 5), "Click again to close")
    close_win.draw(win)
    win.getMouse()
    win.close()


def pi2():
    number_to_sum = eval(input("enter the number of terms to sum: "))

    acc_denom = 3
    pi_approx = 4
    sign_change = 1
    acc_sum = 0

    for _ in range(number_to_sum):
        pi_approx = pi_approx + acc_sum

        sign_change = (-1) * sign_change
        acc_sum = sign_change * (4 / acc_denom)

        acc_denom = acc_denom + 2

    accuracy = abs(math.pi - pi_approx)

    print("pi approximation:", pi_approx)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    pass
