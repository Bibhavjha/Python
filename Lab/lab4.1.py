# Create a function that takes radius of circle as input from the user and return the area.
def circle(r):
    return 3.14*r**2
    
r=int(input("Enter radius of circle"))
print(circle(r))