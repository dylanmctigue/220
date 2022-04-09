"""
Name: Dylan McTigue
face.py

Problem: Create functions that use decision and repetition structures, boolean values,
and create classes and objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Line, Polygon, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.eye_size = eye_size
        self.center = center
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.point_1 = point_1
        self.point_2 = point_2
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        point_3 = self.center.clone()
        point_3.move(0, self.point_2.getX() - self.point_1.getX())
        self.mouth = Polygon(self.point_1, self.point_2, point_3)
        self.mouth.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        point_3 = self.center.clone()
        point_3.move(0, (self.point_2.getX() - self.point_1.getX()) / 2)
        self.mouth = Circle(point_3, self.eye_size)
        self.mouth.draw(self.window)

    def wink(self):
        self.left_eye.undraw()

        left_center = self.left_eye.getCenter()
        left_center_x = left_center.getX()
        left_center_y = left_center.getY()
        left_radius = self.left_eye.getRadius()
        point_1_x = left_center_x - left_radius
        point_2_x = left_center_x + left_radius
        point_1 = Point(point_1_x, left_center_y)
        point_2 = Point(point_2_x, left_center_y)
        self.left_eye = Line(point_1, point_2)

        point_3 = self.center.clone()
        point_3.move(0, self.point_2.getX() - self.point_1.getX())
        self.mouth = Polygon(self.point_1, self.point_2, point_3)

        self.left_eye.draw(self.window)
        self.mouth.draw(self.window)
