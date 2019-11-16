# *args and **kwargs

def function1(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("Now some of the heros are:\n")
    for key, value in kwargs.items():
        print(key,value)

har=["a","b","c"]
normal="This is normal agrument"
kw={"Rohan":"monitor","harry":"gym mate"}
function1(normal,*har,**kw)


