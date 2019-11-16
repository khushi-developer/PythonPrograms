# if else elif statement

var1=33
var2=56
"""
print("Enter number")
var3=int(input())

if var3>var2:
    print("greater")

elif var3==var2:
    print("Equal")

else:
    print("lesser")

print("------------------------------------")
"""
#in keyword nd not in keyword
"""
list1 = [1,3,5,7,9]

print(5 in list1)
print(2 not in list1)
if 5 in list1:
    print("present")

elif 5 not in list1:
    print("2 not in list")

else:
    print("not present")

print("-----------------------------------------")
"""

print("Enter Age")
age=int(input())
if age>7 and age<100:

    if(age<18):
         print("you cannot drive")

    elif(age==18):
        print("we think about you")

    else:
         print("You can drive")

print("you havent entered age is inbetween 7 to 100")