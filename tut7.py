var1 = "Hello world"
var4= "33"
var5= "33"
var2 = 7
var3 = 33.7
print(type(var1))#print the type of variable

print("---------------------------")

print(var2+var3)
print(var1+var4)
print(var4+var5)
print(var4)

print("---------------------------")

print(10 * "hellow\n") #print var1 10 times
print(10 * var2)  #cz of var2 is int variable it multiplies it by 10
print(10 * str(var2)) #by converting int var to string print 7, 10 times

print("---------------------------")
"""
for type casting
Str(variable)
int(variable)
float(variable)
"""

print(int(var4))
print(int(var4)+int(var5))
print(int(var4)+var2)

print("---------------------------")

print("Enter number\n")
num1 = input()

print("Enter number\n")
num2 = input()

print(int(num1)+int(num2))

print(int(num1)+10)
