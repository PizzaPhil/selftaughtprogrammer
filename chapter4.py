# Challenges
#1
def int_square() :
    # this will take an int or float and square it
    x = input("please enter a number: ")
    try :
        print(str(x) + " squared is " + str(  float(x) ** 2) )
    except (TypeError, ValueError):
        print("That's not a number")
        int_square()

int_square()

#2

def prnt_str() :
    #prnt_str() takes the input which is, by default, a string, and prints it uppercase
    var = input("Please enter something and I will print it in uppercase: ")
    var = var.upper()
    print(var)

prnt_str()

 #3
def func3(a, b, c, d=1, e=1) :
    #This function i gave 3 perameters and 2 optional perameters
    try :
        print(a * b * c * d * e)

    except (TypeError, ValueError) :
        print("please, numbers only")
func3(1,2,3,4,5)

#4

def func4() :
    #func4() makes a global var2, if your input is an int then it will divide by 2
    global var2
    var2 = input("please enter an integer: ")
    try :
        return (int(var2) / 2)
    except  (TypeError, ValueError) :
        print("it has to be an integer please")
        func4()

def func5(var2) :
    #func5 takes the result of func4() and divides it by 4
    print(var2 / 4)

func5(func4())

#5
def makefloat() :
    #makefloat() takes an input that is an int or float and prints it as a float
    x = input("please enter a number: ")
    try :
        print(float(x))
    except (TypeError, ValueError) :
        print("I said a number")
        makefloat()

makefloat()
