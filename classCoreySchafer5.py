# SPECIAL METHOD / MAGIC METHODS / DUNDER METHODS IN PYTHON OOP

# these are used to implement operator overloading and change the behaviour of displaying objects
# __init__ method is also a special/dunder method

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # defining __repr__() method    
    def __repr__(self) -> str:
        return "Employee('{}', '{}' , '{}')".format(self.first, self.last, self.pay)
    
    # defining __str__() method
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
    
    # suppose we want to add salaries of two employees
    def __add__(self, other):
        return self.pay + other.pay
    
    # suppose we want to number of characters in fullname
    def __len__(self):
        return len(self.fullname())
    
    
    
# instances of Employee class
emp_1 = Employee('ishu', 'pandey', '50000')
emp_2 = Employee('test', 'user', '20000')

# after defining __repr__() the below line changes behaviour, it prints the details of emp_1
# after defiining __str__() the line below executes according to __str__() method
# print(emp_1)

# to access them individually
# print(repr(emp_1))
# print(str(emp_2))

# what is happening here -->
# print(emp_1.__repr__())
# print(emp_1.__str__())

# dunder add method for int and str
# print(int.__add__(1,2))
# print(str.__add__('abbbd', 'eddjjckb'))

# adding salaries of two employees through __add__() method
print(emp_1 + emp_2)

print(len("test_lenght"))
print("test_lenght".__len__())

# printing length of emp_1 fullname
print(len(emp_2))








