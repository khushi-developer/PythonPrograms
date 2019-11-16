#function and doc string
# we can click on user defined function nd press crtl key nd open the function implementation

v= sum((1,2)) #build in function
print(v)

def function1():  #user defined function
    print("This is function 1")

def function2(a,b):
    """ This function performs addition of two numbers
    We cannot perform addition of 3 numbers here"""
    return a+b

print(function2.__doc__)
print("This is Addition of two numbers",function2(2,3))

#function1()