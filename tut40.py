# Exercise - 6

import random
c=0
u=0
i=0
while( i<3):

    ch = input("Enter in betn snake(s) ,water(w) ,gun(g)")
    # print(ch)

    lst = ["s", "w", "g"]
    p = random.choice(lst)
    print(p)

    if ch=='s' and p=='g':
        print("computer won")
        c=c+1
    elif ch=='w' and p=='s':
        print("computer won")
        c = c + 1

    elif ch=='w' and p=='g':
        print("user won")
        u=u+1

    elif ch=='g' and p=='w':
        print("computer won")
        c = c + 1

    elif ch=='g' and p=='s':
        print("user won")
        u=u+1

    elif ch=='s' and p=='w':
        print("user won")
        u=u+1

    else:
        print("tie")
    i+=1

if(u>c):
    print("user won by score ",u-c)

else:
    print("computer won by score",c-u)
