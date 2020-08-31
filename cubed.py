#!  this is a module that returns the cube of a number. takes one parameter

def cube(x) :
    if (type(x) == int) or (type(x) == float) :
        print(x ** 3)
    else :
        print("please enter an integer or a float")

