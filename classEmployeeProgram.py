# classes, instances and instance variables
# video notes by corey schafer python oop tutorial 1
class Employee:

    # class variable
    # can be accessed through class name or instances
    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_emp +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



        
# instances  of class Employee
emp1 = Employee('suryamani','pandey', 80000)
emp2 = Employee('chandramani','pandey',60000)

# print(emp1)
# print(emp2)

# creating Instance/object variables for emp1
# emp1.first = 'surya'
# emp1.last = 'pandey'
# emp1.email = 'surya.pandey@company.com'
# emp1.pay = 50000

# creating Instance variables for emp2
# emp2.first = 'chandra'
# emp2.last = 'pandey'
# emp2.email = 'chandra.pandey@company.com'
# emp2.pay = 40000

print(emp1.email)
print(emp2.email)

print(emp1.fullname()) # using instance directly

print(Employee.fullname(emp1)) # using class and passing on instance/object

# applying raise 
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# checking out raise amount value
print(emp2.raise_amount)
print(Employee.raise_amount)

# access the namespace of emp1
print(emp1.__dict__)

# printing number of employees
print(Employee.no_of_emp)


 





 