#string methods
a = " Hello, World! "
b= "I am a String with no strings attached"

# length of a string
print(len(a))


print(a.replace("He"," adol"))
print(a.lower())
print(a.upper())
print(a.replace("!"," ?? ghoor kya rha hai"))
print(a.strip())
print(a.split(" "))

#string concat
c=a+" "+b
print(c)

print(type(b))

#format strings and placeholders
age = 36
sex=1
txt = "My name is John, I am " + str(age)
print(txt)
txt = "My name is John, I am {} years old, I am {}: that means male"
print(txt.format(age, sex))

quantity = 3
item_no = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, item_no, price))
#formatting with using index numbers
myorder2 = "I want to pay {2} dollars for {0} pieces of item no {1}"
print(myorder2.format(quantity, item_no , price))

#escape characters

#lstrip method 
txt = "     banana     "

x = txt.lstrip()
y = x.rstrip()

print("of all fruits", y , "is my favorite")

#index method returns the first occurance of specified char or string
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
#2
txt = "Hello, welcome to my world."

x = txt.index("e")

print(x) 

#istitle() merhod 
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#join method for strings
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


