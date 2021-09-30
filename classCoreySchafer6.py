# PROPERTY DECORATORS IN OOP - PYTHON --> GETTERS , SETTERS, DELETERS

class Employee:
    # raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@company.com"
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # to access email as an attribute and not as a method
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    # to access fullname property as a setter 
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    # to access fullname property as a deleter 
    @fullname.deleter
    def fullname(self):
        print('Deleting Name ! ')
        self.first = None
        self.last = None
       
    
emp_1 = Employee('john' , 'smith')
# it will not change email
# emp_1.first = 'Jojo'
# print(emp_1.email)
# print(emp_1.first)

# it will change email as well but has to be accessed as a method
# emp_1.first = 'Jojo'
# print(emp_1.email())
# print(emp_1.first)

## it will change email as well but can be accessed as an attribute
# emp_1.first = 'Jojo'
# print(emp_1.email)
# print(emp_1.fullname)

# after defining SETTER for fullname
# it will set new fullname and first and last name as well for an instance
# notice it has set new values to all the attributes of instance emp_1
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)

# accessing DELETER
del emp_1.fullname

print(emp_1.fullname)
print(emp_1.first)
print(emp_1.email)









