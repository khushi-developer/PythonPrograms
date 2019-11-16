n=int(input("Enter number of test cases"))
numbers=[]

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n=n+1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

for i in range(n):
    number=int(input("Enter the number"))
    numbers.append(number)
print(numbers)
numbers2=[]
for i in range(n):
        if numbers[i]>10:
            print(f"The next palindrome of {numbers[i]} is {next_palindrome(numbers[i])}")
            numbers1 = next_palindrome(numbers[i])
            numbers2.append(numbers1)
        else:
            print(f"{numbers[i]} is less than 10")
            numbers2.append(numbers[i])

        continue

print(numbers2)