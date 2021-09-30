# it is a small anonymous function with only one expression
# can take any number of arguments
# syntax :- lambda arguments : expression
x = lambda a : a + 10
print(x(5))

# with multiple args
x = lambda a,b : a * b
print(x(10.5,20.5))
print(x(5,6))
print(x(0,1999))

# another example
x = lambda a,b,c : (a+b) * c
print(x(5,6,3))

# another use case -- inside a function
# always return the double of the no you send in
def myfunc(n):
    x = lambda a : a * n
    return x

x = myfunc(2)
print(x(17))

# for tripling 
def myfunc(n):
    return lambda a : a * n

x = myfunc(3)
print(x(17))

# use same func for both 
def myfunc(n):
    return lambda a : a * n

x = myfunc(2)
y= myfunc(3)

print(x(14))
print(y(21))