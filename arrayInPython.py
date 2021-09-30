# no built in support for arrays , lists can be used
# import numpy to work with arrays
 
cars = ['bmw', 'ford', 'ferrari', 'mini']
# access items
print(cars[0])
print(cars[2])

# modify items just like lists
cars[0] = 'toyota'
print(cars[0])

# length of an array
x = len(cars)
print(x) 

# looping through array elements
for x in cars:
    print(x)

# adding array element to the end of array
cars.append("hyundai")
print(cars)

# removing array elements
cars.pop(1) # removes element at index 1
print(cars)
cars.pop() # removes last element
print(cars)

# adding elements to array
cars.append("ford")
cars.append('hyundai')
print(cars)

# removing elements using remove() method
# remove() only remove first occurence of specified value
cars.remove('hyundai')
print(cars)

# more array methods
# same as list methods, refer to list methods 
cars.clear() # empties array
print(cars)

# extend method
fruits = ['apple', 'banana', 'cherry','volvo']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits.insert(1,'jaguar')
print(fruits)

fruits.reverse()
print(fruits)

x = fruits.index('banana')
print(x)

x = fruits.count('volvo')
print(x)

# sort methods
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

# sort the list by the length of values and reversed
def myFunc(e):
    return len(e)

fruits.sort(reverse=True, key= myFunc)
print(fruits)

fruits.sort(key = myFunc)
print(fruits)








