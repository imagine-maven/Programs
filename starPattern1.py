# right angle triangle star pattern

n = int(input("enter the value of n: "))

for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print()

