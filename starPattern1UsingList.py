# function to print star pattern using lists
def myPattern(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*" * i)
    #join method to join items into a string using newline 
    #character as a separator
    print ("\n".join(myList))


#driver code
n=10
myPattern(n)
