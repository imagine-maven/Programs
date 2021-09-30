# create a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def calcAge(self):
        age = len(self.firstname) + len(self.lastname)+ 10 
        print(age)

# Use the Person class to create an object
obj1 = Person('surya', "pandey")
obj1.printname()
obj1.calcAge()

# create a child class
# class Student is a derived class of class Person
class Student(Person):
    # The child's __init__() function overrides the inheritance of the parent's __init__() function
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# create object of class Student with all the methods and properties of class Person
obj2 = Student("chandra","pandey", 2021)
obj2.printname()
obj2.calcAge()

obj3 = Student("walter", "white", 2019)
obj3.welcome()



        