# tut-32
# 3 client - rohan ,harry , hammad
# 2 types - exsercise,diet plan

import datetime
def gettime():
    return datetime.datetime.now()

type=input("what you have to do"
           "1.store\n"
           "2.retrive")


ch = int(input("Enter your choice\n 1.Rohan"
               "\n2.Harry"
               "\n3.ahmad"))

part = int(input("Enter your part\n 1.Exsercise"
               "\n2.Diet plan"))
def take(ch):
        if ch==1:
            file= open("rohan.txt","a")

            if part==1:
                content=input(print("Enter exsercise you done"))
                file.write("Exercise")
                file.write(str([str(gettime())]))
                file.write(content)
                print("successfully written")
            else:
                content=input(print("Enter your diet plan"))
                file.write("Diet plan")
                file.write(str([str(gettime())]))
                file.write(":")
                file.write(content)
                print("Successfully written")
            file.close()

        elif ch==2:
            file= open("harry.txt","a")
            if part==1:
                content=input(print("Enter exsercise you done"))
                file.write("Exercise")
                file.write(str([str(gettime())]))
                file.write(content)
                print("successfully written")
            else:
                content=input(print("Enter your diet plan"))
                file.write("Diet plan")
                file.write(str([str(gettime())]))
                file.write(":")
                file.write(content)
                print("Successfully written")
            file.close()

        else:
            file= open("ahmad.txt","r+")
            if part==1:
                content=input(print("Enter exsercise you done"))
                file.write("Exercise")
                file.write(str([str(gettime())]))
                file.write(content)
                print("successfully written")
            else:
                content=input(print("Enter your diet plan"))
                file.write("Diet plan")
                file.write(str([str(gettime())]))
                file.write(":")
                file.write(content)
                print("Successfully written")
            file.close()


def retrive(ch):
        if ch==1:
            if part==1:
                f=open("rohan.txt")
                for i in f:
                    print(i,end=" ")
                f.close()

            else:
                with open("rohan.txt") as op:
                    for i in op:
                        print(i,end=" ")

        elif ch==2:
            if part == 1:
                f = open("harry.txt")
                for i in f:
                    print(i, end=" ")
                f.close()

            else:
                with open("harry.txt") as op:
                    for i in op:
                        print(i, end=" ")
        else:
            if part == 1:
                f = open("ahmad.txt")
                for i in f:
                    print(i, end=" ")
                f.close()

            else:
                with open("ahmad.txt") as op:
                    for i in op:
                        print(i, end=" ")

if type==1:
    take(ch)
else:
    retrive(ch)