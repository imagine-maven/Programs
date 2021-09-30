#list allows duplicates since it is indexed
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(type(thislist)) #find the type

print(thislist)
print(len(thislist)) #length of list

#data types in list- can be of any data type

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# can contain different data types
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# the list constructor
thislist = list(("apple","banana", "cherry")) #double rounded brackets
print(thislist)

# access list itmes
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[2])

# access list items using negative indexing
# -1 is the last item
print(thislist[-1])
print(thislist[-2])

#using range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5]) # 2nd index included 5th not included
print(thislist[:5]) #from beginning, 5th not included
print(thislist[2:]) #from 2nd index till the end
print(thislist[:]) # access whole list

# using range of negative indexes
print(thislist[-4:-1]) # from orange(-4) to but not including mango(-1)
print(thislist[-4:]) # from -4 till last item
print(thislist[:-2]) # from beginning till -2 (-2 melon not included)

# check if item exists in a list
if "orange" in thislist:
	print(True)
    
# change an item value in a list 

thislist[1] = "blackcurrant"
print(thislist)
# change a range of value items
thislist[2:5] = ["watermelon", "muskmelon", "grapes"]
print(thislist)
#adding more items than specified
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining #items will move accordingly-
thislist[1:2] = ["blackcurrant", "watermelon"] 
print(thislist) 

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining #items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert new items using insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# add an item to the end of the list using append() method
thislist.append("blackberries")
print(thislist)

#To append elements from another list to the current list, use the extend() method
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

# using extend() method to add any iterable like tuples, sets, dicts
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove list item using remove() method

thislist.remove("banana")
print(thislist)
# remove item using pop method
thislist.pop(1)
print(thislist)
thislist.pop() #removes the last item
print(thislist)

# remove item using del keyword
del thislist[0]
print(thislist)

del thislist #deletes the entire list
# print(thislist) #generates an error

# empty the list using clear() method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop through the index numbers
for i in range(len(thislist)):
  print(i,":",thislist[i])
  
#by using a while loop 
i=0
while i< len(thislist):
  print(thislist[i])
  i=i+1
  
#loop using list comprehensions
[print(x) for x in thislist]

#LIST COMPREHENSION -------

# syntax : newlist = [expression for item in iterable if condition == True]

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist=[]

# creating a new list with existing elements of previous list with and without using comprehension

#without using list comprehension
#newlist with elements with a "a" in them
for x in fruits:
	if "a" in x:
		newlist.append(x)
print(newlist)

#with using list comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [ x for x in fruits if x != "apple"]
print(newlist)

# with no if statement
newlist = [x for x in fruits]
print(newlist)

# using range function as iterable 
newlist = [x for x in range(11)]
print(newlist)
newlist = [x for x in range(1,20) if x < 15]
print(newlist)
newlist= [x.upper() for x in fruits]
print(newlist)

#victory
newlist = ["Hello "+ str(x.upper()) for x in fruits ]
print(newlist)

newlist = [x if x !="banana" else "eat me" for x in fruits]
print(newlist)

# SORT LISTS with sort() method
fruits.sort() # sort alphanumerically
print(fruits)

fruits.sort(reverse = True) # sort in descending order
print(fruits)

thislist =[100,50,58,46,101]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# case insensitive sort
thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse the  order of a  list\
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# COPY A LIST
thislist = ["apple", "banana", "cherry"]
newlist= thislist.copy() #method 1
print(newlist)

newlist = list(thislist) #method 2
print(thislist)

# JOIN LISTS
list1= ["a","b,","c","d"]
list2= [1,2,3]

list3= list1+list2 #method 1
print(list3)

#using the append method
for x in list2:
	list1.append(x)
print(list1)

#using extend method
list1.extend(list2)
print(list1)

