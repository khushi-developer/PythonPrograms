#try except in python


a=input("Enter a\n")
b=input("Enter b\n")

try:
    print("Addition is",int(a)+int(b))

except Exception as e:
    print(e)


print("This is importat")