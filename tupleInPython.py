# tuple in python demo code
# ordered and unchangeable
# written with round brackets
# allows duplicate values
# unchangeable -- we cannot change, add or remove items after the tuple has been created

thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# accessing items
print(thistuple[2])  
print(thistuple[-1]) # last item
print(thistuple[1:3]) # using range of indexes
print(thistuple[:4])
print(thistuple[2:])
# using negative indexing
print(thistuple[-4:])
print(thistuple[-4:-1])
print(thistuple[-1:-4]) # returns empty tuple bcz of wrong way of indexing


print(len(thistuple))  # finding length
print(type(thistuple))  # finding type

# creating tuple with only one element
mytuple = ("suryamani",)  # remeber the comma
print(type(mytuple))  # class 'tuple'

mytuple = ("pandey")
print(type(mytuple))  # class 'str'

# allowed data types in a tuple -- any
tuple1 = ('apple', 'banana', 'kiwi')
tuple2 = (1, 5, 89, 65, 25)
tuple3 = (True, False, True, True, False)
# tuple containing different data types
tuple4 = ('surya', 24, True, 'male')

print('\n', tuple1, '\n', tuple2, '\n', tuple3, '\n', tuple4)

print(type(tuple4))

# tuple constructor with double rounded brackets
thistuple = tuple(('surya','eats','apple','all the time'))
print(thistuple)
print(type(thistuple))

# check if item exist
if "surya" in thistuple:
    print(True)
else:
    print(False)

# change tuple values by converting them to a list and then converting back to a tuple
newlist = list(thistuple)
newlist[1]='eats and treats'
newlist.append("he\'s so fit")
thistuple = tuple(newlist)
print(thistuple)

# adding tuples is allowed however
tuple4 += thistuple
print(tuple4)
print(type(tuple4))

# remove items by converting them to a list and then converting back to a tuple
list2 = list(tuple4)
list2.pop(4)
tuple4 = tuple(list2)
print(tuple4)

# delete the tuple completely
del tuple4
# print(tuple4) # this will produce an error

# unpacking a tuple
# extract the values back into variables. This is called "unpacking"
fruits = ('apple','banana','cherry')
(green,yellow,red) = fruits
print('green:',green)
print(yellow)
print(red)

# using asterisk
# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list
fruits = ("apple", "banana", "cherry", "strawberry","raspberry")
(green,yellow,*red)= fruits
print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# loop through a tuple
thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

# Loop Through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])

# using while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1

# join tuples using +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1+tuple2
print(tuple3)

# multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# tuple methods

# count method
thistuple = (1, 3, 7, 8, 7, 5, 5, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index method
x = thistuple.index(8)
print(x)
















