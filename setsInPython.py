# code demonstrating sets and their uses
# unordered and unindexed and unchangeable
# no duplicate items
# the order of items on display keeps changing
myset = { 'apple', 'banana', 'kiwi'}
print(myset)
print(type(myset))

print(len(myset))

# can contain any data type or even mixed types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"} 
print(set1)
print(set2)
print(set3)
print(set4)
print(type(set4))

# set constructor
thisset = set(('apple','orange','guava','papaya','lemon'))
print(type(thisset))

# access set items use loop
# cannot access using index as there is no indexing 
for x in thisset:
    print(x)

# check if element is present
if 'orange' in thisset:
    print(True)

print('banana' in thisset) 
print('guava' in thisset)

# cannot change items but can add new items
thisset.add('banana')
print(thisset)

# add sets together
tropical = { 'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

# add any iterable
mylist = ['grass','leaves']
thisset.update(mylist)
print(thisset)
print(type(thisset))

# remove item using remove() and discard()
thisset.remove('banana')
print(thisset)
# If the item to remove does not exist, remove() will raise an error
# thisset.remove('kela')
# print(thisset)

thisset.discard('guava')
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error
thisset.discard('kela')
print(thisset)

# using pop()
x = thisset.pop()
print("item popped is : ", x)
print(thisset)

# clear method empties the set
thisset.clear()
print(thisset)

# del keyword deletes the set 
del thisset
# print(thisset)  # generates error

# loop sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# join sets
set1 = {'a','b','c'}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

# update() method inserts the items in set2 into set1
set1.update(set2)
print(set1)

# keep only the duplicates
x = {"apple", "banana", "cherry",'kiwi'}
y = {"google", "microsoft", "apple",'amazon','kiwi'}

x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry",'kiwi'}
y = {"google", "microsoft", "apple",'amazon','kiwi'}

# Keep All, But NOT the Duplicates
# updates the set x
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets

x = {"apple", "banana", "cherry",'kiwi'}
y = {"google", "microsoft", "apple",'amazon','kiwi'}
k = x.symmetric_difference(y)
print(k)

# set methods

# Python Set copy() Method
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# difference method
# Return a new set that contains the items that only exist in set x, and not in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# difference_update method Remove the items that exist in both sets:
x.difference_update(y)
print(x)

# isdisjoint() Method : Return True if no items in set x is present in set y
z = x.isdisjoint(y)
print(z)

# issubset() Method Return True if all items in set x are present in set y
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# isusperset method Return True if all items set x are present in set y
z = y.issuperset(x)
print(z)

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) 





