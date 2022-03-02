"""
Name: Dylan McTigue
lab7.py

Problem: Create program that creates circles and shows them endlessly bumping off of each other
and the walls using several functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Point, GraphWin, color_rgb
from random import randint
import math
import time

def get_random(move_amount):
    random_int = randint(-move_amount, move_amount)
    return random_int

def did_collide(ball, ball_2):
    ball_center = ball.getCenter()
    ball_2_center = ball_2.getCenter()

    ball_x = ball_center.getX()
    ball_2_x = ball_2_center.getX()
    ball_y = ball_center.getY()
    ball_2_y = ball_2_center.getY()

    distance = math.sqrt(((ball_2_x - ball_x) ** 2) + ((ball_2_y - ball_y) ** 2))

    radius_sum = ball.getRadius() + ball_2.getRadius()

    boolean_value = distance < radius_sum

    return boolean_value

def hit_verticle(ball, win):
    ball_center = ball.getCenter()
    ball_y = ball_center.getY()

    win_height = win.getHeight()

    radius = ball.getRadius()

    if ball_y + radius >= win_height or ball_y <= radius:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    ball_x = ball_center.getX()

    win_width = win.getWidth()

    radius = ball.getRadius()

    if ball_x + radius >= win_width or ball_x <= radius:
        return True
    else:
        return False

def get_random_color():
    random_color = color_rgb(randint(0, 225), randint(0, 225), randint(0, 225))
    return random_color

def Bumper():
    win = GraphWin("Bumper", 700, 700)

    circle_1 = Circle(Point(randint(20, win.getWidth() - 20), (randint(20, win.getHeight() - 20))), 20)
    circle_2 = Circle(Point(randint(20, win.getWidth() - 20), (randint(20, win.getHeight() - 20))), 20)

    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())

    circle_1.draw(win)
    circle_2.draw(win)

    circle_1_move_x = get_random(10)
    circle_1_move_y = get_random(10)
    circle_2_move_x = get_random(10)
    circle_2_move_y = get_random(10)

    while not win.checkMouse():
        circle_1.move(circle_1_move_x, circle_1_move_y)
        circle_2.move(circle_2_move_x, circle_2_move_y)

        if did_collide(circle_1, circle_2):
            circle_1_move_x = circle_1_move_x * -1
            circle_1_move_y = circle_1_move_y * -1
            circle_2_move_x = circle_2_move_x * -1
            circle_2_move_y = circle_2_move_y * -1

        if hit_verticle(circle_1, win):
            circle_1_move_y = circle_1_move_y * -1

        if hit_verticle(circle_2, win):
            circle_2_move_y = circle_2_move_y * -1

        if hit_horizontal(circle_1, win):
            circle_1_move_x = circle_1_move_x * -1

        if hit_horizontal(circle_2, win):
            circle_2_move_x = circle_2_move_x * -1

        time.sleep(.01)

    win.close()
Bumper()