# a=input("what is your name")
# b=input("How much you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"hellow {a}")
# 1000 lines take 1hr

# task - 2 Exception

c=input("Enter name")
try:
    print(a)

except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked . he is not allowed")
    print("Exception handled")