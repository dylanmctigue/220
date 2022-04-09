"""
Name: Dylan McTigue
sphere.py

Problem: Create functions that use decision and repetition structures, boolean values,
and create classes and objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)
