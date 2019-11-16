"""
a=20
def function1():
    #a=30
    global a
    a=a+15
    print("a is",a);

function1()
print(a)
"""

def function1():
    a=30
    def function2():
        global a
        a=88
        print(a)
    print("a is",a);
    function2()
    print("a is", a);

function1()
print(a)

