def foo(k):
    if (k > 0):
        result = k + foo(k-1)
        print(result)
    else:
        result = 0
    return result

#driver code
foo(7)
