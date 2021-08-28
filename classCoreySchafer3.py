# class methods and static methods


class Employee:

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1

    # regular methods that takes instance as first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # creating a class-method
    # cls is the common convention like self
    # class-method will recieve class as first arg
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True



emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('surya', 'mani', 60000)

Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# creating new employees from string parsing
# emp_str_1 = 'john-doe-70000'
# emp_str_2 = 'steve-smith-30000'
# emp_str_3 = 'jane-doe-90000'

# method-1
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.first,new_emp_1.last)
# print(new_emp_1.email)

# method-2
# new_emp_1 = Employee.from_string(emp_str_3)
# print(new_emp_1.first,new_emp_1.last)
# print(new_emp_1.pay)

# checking out our static method
import datetime
my_date = datetime.date(2022, 7 , 28)
print(Employee.is_workday(my_date))



