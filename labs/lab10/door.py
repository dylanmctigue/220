"""
Name: Dylan McTigue
door.py

Problem: Create Door Class tto encapsulate data in a graphics window,
which allows the user to click the door and open and close it

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text


class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        corner_one = self.shape.getP1()
        corner_two = self.shape.getP2()

        x_one = corner_one.getX()
        x_two = corner_two.getX()

        y_one = corner_one.getY()
        y_two = corner_two.getY()

        point_x = point.getX()
        point_y = point.getY()

        if (x_two >= point_x >= x_one) and (y_two >= point_y >= y_one):
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret
