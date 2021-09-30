# INHERITANCE IN PYTHON

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
        # self.pay = int(self.pay * Employee.raise_amount)

# creating a sub class of Employee
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # method to call parent class init method
        super().__init__(first, last, pay)
        # the method below is also true
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
       def __init__(self, first, last, pay, employees=None):
           # setting None as default value for number of employees
           super().__init__(first, last, pay)
           if employees is None:
               self.employees = []
           else:
               self.employees = employees
       # adding new emp to managing list
       def add_emp(self,emp):
           if emp not in self.employees:
               self.employees.append(emp)
               
       def remove_emp(self,emp):
           if emp in self.employees:
               self.employees.remove(emp)
               
       def print_emp(self):
           for emp in self.employees:
               print('-->', emp.fullname())
               
           
# instances of Developer class
dev_1 = Developer('ishu','pandey','50000', 'python')
dev_2 = Developer('test','user','20000', 'java')

# devdeloper class instances accessing all functionality of employee class
print(dev_1.email)
print(dev_2.fullname())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# print(help(Developer))

print(dev_2.prog_lang)

# instances of Manager  class
mgr_1 = Manager('sue', 'smith', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.print_emp()

mgr_1.add_emp(dev_2)
mgr_1.print_emp()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

# two imp built-in functions of python
# isinstance() results in boolean true or false
print(isinstance(mgr_1, Manager))
print(isinstance(dev_1, Employee))
print(isinstance(mgr_1, Employee))
print(isinstance(dev_1, Manager))

# issubclass() results in boolean true or false
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))






      








