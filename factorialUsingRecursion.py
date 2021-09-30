
# using recursion
def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
    

#driver code  
n = 1
print(fact(n))

n = 0 
print(fact(n))

n = 4
print(fact(n))

n = 5
print(fact(n))

n =7
print(fact(n))

n = 10
print(fact(n))

