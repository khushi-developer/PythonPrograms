# Exsercise-4
# pattern printing

n=int(input("Enter number"))
bool_val=int(input("Have u want to print then press 1/0"))

if bool_val==1:
    while(n>0):
        print(n*"*")
        n = n-1

else:
    p1=1
    while (n > p1):
        print(p1 * "*")
        p1 = p1 + 1
