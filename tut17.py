#while loop
"""
i=0
while i<45:
    print(i,end=" ")
    i=i+1
"""

#tut 18 Break and continue statement
"""
i=0
while(True):
    if i+1<5:
        i=i+1
        continue

    print(i+1,end=" ")
    if i==44:
        break
    i=i+1
"""
print("--------------------------------------")


while(True):
    print("Enter number")
    i = int(input())
    if i<=100:
        print("Try again!")
        continue

    else:
        print("congo,you enter number which is greater than 100")
        break

