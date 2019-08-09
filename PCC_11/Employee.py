class Employee():
    """ store the emplyee's first, last name and salary"""

    def __init__(self, first_name, last_name, an_salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.an_salary = an_salary

    def give_raise(self, raise_num=5000):
        self.an_salary = self.an_salary + raise_num

