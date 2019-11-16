# try:
#     n=int(input("Enter number of test cases"))
#
#     for i in range(n):
#         s = input("Enter string or number:")
#         if(s==s[::-1]):
#             print("String or number is palindrome")
#         else:
#             print("String or number is not palindrome")
#
# except Exception as e:
#     print("please enter valid input : ",e)

n = int(input("Enter number of test cases"))
numbers=[]

def next_palindrrome(n):
    n+=1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    for i in range(n):
        number=int(input("enter number"))
        numbers.append(number)

for i in range(n):
    print(f"Next palindrome of {numbers[i]} is {next_palindrrome(numbers[i])}")

