"""
Name: Dylan McTigue
lab4.py

Problem: I need to create a valentine's day card that displays a heart and a greeting,
then an arrow that shoots through the heart. It will then say "click to close"
and the user can click to close the window.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from graphics import Point, GraphWin, Circle, Text, Entry, Polygon


def greeting_card():

    win = GraphWin("Valentine's Day Card", 600, 800)
    win.setCoords(0, 0, 6, 8)

    heart = Polygon(Point(3, 4), Point(3.5, 4.5), Point(3.9, 5),
                            Point(4.5, 6), Point(4.4, 6.5), Point(4, 7), Point(3.75, 7.1),
                            Point(3.5, 7), Point(3, 6.6), Point(2.5, 7), Point(2.25, 7.1),
                            Point(2, 7), Point(1.6, 6.5), Point(1.5, 6), Point(2.1, 5),
                            Point(2.5, 4.5), Point(3, 4))

    arrow = Polygon(Point(1, 1), Point(1.5, 1.5), Point(1.375, 1.625), Point(2.375, 2.625),
                             Point(2.5, 2.5), Point(2.625, 3), Point(2.125, 2.875), Point(2.25, 2.75),
                             Point(1.25, 1.75), Point(1.125, 1.875), Point(0.625, 1.375), Point(1, 1.375))

    arrow.move(-2.5, 0)

    win.setBackground("pink")
    arrow.setFill("blue")
    heart.setFill("red")

    greeting = Text(Point(3, 2), "Happy Valentine's Day!")
    greeting.setTextColor("green")
    greeting.setStyle("bold italic")
    greeting.setSize(36)

    click_to_close = Text(Point(3, 1), "Click to Close")

    heart.draw(win)
    arrow.draw(win)
    greeting.draw(win)


    for i in range(75):
        arrow.move(.1, .1)
        time.sleep(.1)

    click_to_close.draw(win)

    win.getMouse()

greeting_card()