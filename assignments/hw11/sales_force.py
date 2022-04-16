"""
Name: Dylan McTigue
sales_force.py

Problem: Write a class that encapsulates data for a sales person that includes
sales_people as instance variables, and can give information about them.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


def word_sort(tup):
    return tup[1]


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        read_file = open(file_name, 'r').readlines()
        for i in range(len(read_file)):
            read_file[i] = read_file[i].split(', ')
            s_person = SalesPerson(int(read_file[i][0]), read_file[i][1])
            sales = read_file[i][2]
            sales = sales[:-1]
            sales = sales.split(' ')
            for j in range(len(sales)):
                s_person.enter_sale(float(sales[j]))
            self.sales_people.append(s_person)
        return self.sales_people

    def quota_report(self, quota):
        sellers_list = []
        for i in range(len(self.sales_people)):
            sale_id = self.sales_people[i].get_id()
            name = self.sales_people[i].get_name()
            total_sales = self.sales_people[i].total_sales()
            hit = total_sales >= quota
            sale_person = [sale_id, name, total_sales, hit]
            sellers_list.append(sale_person)
        return sellers_list

    def top_seller(self):
        top_total = 0
        result = []
        for i in range(len(self.sales_people)):
            each_total = self.sales_people[i].total_sales()
            if each_total == top_total:
                result.append(self.sales_people[i])
            if each_total > top_total:
                top_total = self.sales_people[i].total_sales()
                result = [self.sales_people[i]]
        return result

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            sales_person = self.sales_people[i]
            if sales_person.get_id() == employee_id:
                return sales_person
        return None

    def get_sale_frequencies(self):
        sales = []
        for i in range(len(self.sales_people)):
            sales_person = self.sales_people[i]
            each_sales = sales_person.get_sales()
            sales = sales + each_sales
        count = {}
        for sale in sales:
            if sale in count:
                count[sale] = count[sale] + 1
            else:
                count[sale] = 1
        return count
