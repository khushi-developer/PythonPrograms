#lambda functions anonymous function

# add = lambda a,b : a+b
# print(add(2,3))
#
# # it is same as function
# def add(a,b):
#     return a+b
# print(add(2,3))

def a_first(a):
    return a[1]

a=[[1,4], [11,8],[5,4]]
a.sort(key=a_first)
print(a)