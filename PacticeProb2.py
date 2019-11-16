students=20

try:
    n = int(input("Enter the number of apple got harry"))
    number_of_apples = n/students
    a = n%students
    if a == 0:
        print("Apples are distributed equally",number_of_apples,"to each student")

    else:
        if a>5:
            print("requires",a," more apples to distribute equally")
        else:
            print("Dont requires",a,"apples, it will creates unbalancing")

    mn=int(input("Enter the minumum range"))
    mx=int(input("Enter maximum range"))

    if mn==mx:
        print("maximum and minimum range are equal")

    else:
        if n%mn==0:
            print("Divide by mn",n/mn,"apples distributed in each student. \n number is divisor of",mn)

        else:
            print("Number is not divisor by",mn)

        if n%mx==0:
            print("Divide by mx",n/mx,"apples are distributed in each student. \n number is divisor of",mx)

        else:
            print("Number is not divisor of",mx)

except Exception as e:
    print(e)
