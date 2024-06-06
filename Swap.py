# create a function that swaps the two values provided and returns the swapped values
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b #return as a tuple
print(swap(5,6))
    