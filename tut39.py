# F strings
import time
import math
# me = "Harry"
# a="This is %s"%me
# print(a)


me="khushi"
a1=3
# # a="This is %s %s"%(me,a1)
# a="this is {1} {0}"
# b=a.format(me,a1)
# print(b)

a= f" this is {me} {a1} {math.cos(65)} {time.time()}"
print(a)