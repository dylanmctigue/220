"""
Name: Dylan McTigue
sales_person.py

Problem: Write a class that collects data and presents that data about a sales person.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales = self.sales + [sale]

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return sum(self.sales) >= quota

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() == self.total_sales():
            return 0
        return 1

    def __str__(self):
        return '{}-{}:{}'.format(self.employee_id, self.name, self.total_sales())
