#========================MAP==============================
# num=["34","19","13","143"]
# o=list(map(int,num))
# print(o)
#
# lis=[1,2,3,4]
# o=list(map(lambda x:x*x,lis))
# print(o)
#
# def sq(num):
#     return num*num
# def cube(num):
#     return num*num*num
#
# func=[sq,cube]
# for i in range(5):
#     o = list(map(lambda x: x(i), func))
#     print(o)


# ==========================FILTER======================

lis=[1,2,3,4,5,6,7,8,9]
def isgreater5(num):
    return num>5
o=list(filter(isgreater5,lis))
print(o)


# ===========================REDUCE===================

# lis=[1,2,3,4]
# import functools as f
# o=f.reduce(lambda x,y:x+y,lis)
# print(o)