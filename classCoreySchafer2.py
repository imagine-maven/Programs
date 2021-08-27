# class variables

class Employee:
    #class variable
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        #every time init method runs a new employee is created
        Employee.num_of_emp += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)

# instances  of class Employee
emp_1 = Employee('corey','schafer',50000)
emp_2 = Employee('surya', 'mani',60000)

# print(emp_1.pay)
# print(emp_1.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)

# access the class var through instance   
# print(emp_1.raise_amount) 
# print(emp_2.raise_amount)
# access the class variable through class 
# print(Employee.raise_amount)

# change the raise_amount for class and all of its instances
# Employee.raise_amount = 1.05
# print(emp_1.raise_amount) 
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# change the raise amount for only selected instance
emp_2.raise_amount = 1.04
print(emp_2.raise_amount)

# printing out emp_2 namespace
print(emp_2.__dict__)
# emp_2 has raise amount within it's namespace where emp_2 wouldn't have it


# print(emp_1.pay)
# print(emp_1.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.num_of_emp)
emp_3 = Employee('chandra', "pandey", 75000)
print(Employee.num_of_emp)


