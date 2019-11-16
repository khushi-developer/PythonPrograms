#Excercise 3

n = 18
i=0
while(True):
    if i<5:
        print("Guess the number i have entered")
        num = int(input())

        if num>n:
            print("number is greater","remaining attept are",4-i)
            i=i+1
            continue

        elif num<n:
            print("Number is lesser""remaining attept are",4-i)
            i=i+1
            continue

        else:
            print("congo, u guess perfect number in",i+1,"attempt")
            i=i+1
            break
    break

print("game over")