"""
Name: Dylan McTigue
lab10.py

Problem: Create Button Class and Door Class that encapsulates data in a graphics window,
which allows the user to click the door to open and close it, then press exit when they want
to leave

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

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

        x_point = point.getX()
        y_point = point.getY()

        if (x_two >= x_point >= x_one) and (y_two >= y_point >= y_one):
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
