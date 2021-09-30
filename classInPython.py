# class is like object constructor or a blueprint for creating objects
# class is only used to define the schema, it's like a container
# every variable , method defined here is to be used by objects


# creating class using class keyword
class myClass:
    x = 5

# create objects
p1 = myClass()
print(p1.x)


class Person:
    # All classes have a function called __init__(), which is always executed when the class is being initiated
    # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

    # the self parmeter is a reference to the current instance of the class, and is used to access variables that belongs to the class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        x = 'hello! my name is {} and I\'m {} years old'
        print(x.format(self.name, self.age))
    
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
    def myFunc2(abc):
        x = 'hello! my name is {} and I\'m {} years old'
        print(x.format(abc.name, abc.age))

# creating instances/objects of class person
p1 = Person("vishu", 25)
p2 = Person('ishu', 21)

print(p1.name, p1.age)
print(p2.name, p2.age)

# object method
p1.myFunc()
p2.myFunc()

p1.myFunc2()
p2.myFunc2()

# modify object properties
p1.age = 18
p1.name = 'mimi'
print(p1.age, p1.name)

# delete object properties
del p1.age

# delete objects
del p1
# print(p1.age, p1.name)

# the pass statement : to have a class definition with no content, put in the pass statement to avoid getting an error
class Temp:
    pass

# delete a class
del Temp


