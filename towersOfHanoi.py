# this problem uses recursion
def move(f,t):
    # f : from position
    #t : to position
    print("move disc from {} to {} !".format(f,t))

def moveVia(f,v,t):
    # v : via position
    move(f,v)
    move(v,t)

def hanoi(n,f,h,t):
    #n : number of discs
    # f : from position , h: helper position, t: target position
    if n==0:
        pass
    else:
        #solve the problem for n-1 discs, first move them from posn to helper posn via target posn
        # using recursion
        hanoi(n-1,f,t,h)

        # move the nth disc to target posn from initial(from) posn
        move(f,t)

        # move the remaining n-1 discs from helper to target posn via from posn
        # using recursion
        hanoi(n-1,h,f,t)

#driver code
hanoi(5,"A","B","C")
