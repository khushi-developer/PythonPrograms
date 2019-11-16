# iterative apporch
"""
def fun1(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

print(fun1(5))


# Recursive approach

def fun2(n):
    if n==1:
        return 1
    else:
        return n * fun2(n-1)

no=int(input("Enter number"))
print(fun2(no))
"""
# 0 1 1 2 3 5
a = int(input("Enter number"))
def fiboncciie(n):

     p=0
     for i in range(n):
          print(p, end="\n ")
          p=(i)+(i+1)
          print((i+2))
          # f4 = f3 + f2
          # print(f4)

print(fiboncciie(a))