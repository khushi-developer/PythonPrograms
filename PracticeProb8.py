n = int(input("Enter number"))
numbers = []
for i in range(11):
    f = n * i
    if i == 3:
        numbers.append(f+3)
        continue
    numbers.append(f)
    # print(f)

# print(numbers)

lis = []
for i in range(11):
    f = n * i
    lis.append(f)

# print(lis)

if numbers == lis:
    print("Table is correct!")
else:
    print("Oops,Rohan das table is incorrect!")