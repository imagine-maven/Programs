# classes and instances
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# instances  of class Employee
emp_1 = Employee('corey','schafer',50000)
emp_2 = Employee('surya', 'mani',60000)

# accessing instance variables        
print(emp_1.email)
print(emp_2.first, emp_2.last)

# both lines below will do same thing
# accessing regular method fullname() for object emp_1
print(Employee.fullname(emp_1))
print(emp_1.fullname())

