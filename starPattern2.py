# simple starPattern1 program after a 180 degree rotation
def starPattern2(n):

    for i in range(0,n):
        # k gives the number of spaces
        k= n-i
         
        # inner loop to handle number spaces
        for j in range(0,k):
            print(end=" ")
            
        # inner loop to handle number of columns
        for j in range(0,i+1):
            #this will print right angle triangle
            print("*",end="") 
            
            #this will print triangle
            #print("*",end=" ") 
            
            #this will also print same triangle as above
            #print("* ",end="") 

        print("\r")
n=6
starPattern2(n)
