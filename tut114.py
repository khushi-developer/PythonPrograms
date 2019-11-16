# Exercise 2 faulty calculator

print("Enter number1")
num1=int(input())

print("Enter operator")
op=input()

print("Enter number1")
num2=int(input())

if num1==45 and num2==3 and op=='*':
    print(559)

elif num1==12 and num2==5 and op=='/':
    print(103)

elif num1==99 and num2==3 and op=='+':
    print(113)

elif op=='+' :
    print(num1+num2)

elif op=='-' :
    print(num1-num2)

elif op=='*' :
    print(num1*num2)

elif op=='/' :
    print(num1/num2)
