
print("Hello Everyone , this program tell you when you become 100 years old and aslo tell your age at cuurent year or given year")

cur_year=2019
countage=0

try:

    age = int(input("Enter your current age or Enter your Date of birth"))

    if(age<125 or age<1900):
        print("Invalid age or year")

    elif age<0 and cur_year<age:
        print("You are not yet born")

    elif(len(str(age))==4):
        while(age<cur_year):
            countage = countage + 1
            age+=1
        year100=100 - countage
        print("Your current age is",countage,"After",year100,"you will become 100 years old....in the year",cur_year+year100,"you will becomes the 100 years old")

    elif(len(str(age))==2):
        year100 = 100 - age
        countage=age
        print("After", year100, "years you will become 100 years old...in the year", cur_year + year100,
              "your 100th birthday")

    countage1=0
    your_age_count_at_year = int(input("Enter the year from which you want your age at"))

    if age<cur_year:   #2006<2019
        print("Invalid year")

    while(cur_year<your_age_count_at_year): #2019 2025
        countage1+=1
        cur_year+=1
    print("You will be",countage+countage1,"years old at",your_age_count_at_year)

except Exception as e:
    print("You are not yet born")

except NameError as e1:
    print(e1)


