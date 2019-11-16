#file and its mode nd its operations

file=open("khushi.txt","r")

for line in file:
    print(line,end="") #print whole file line by line
"""
file=open("khushi.txt")
content=file.read(3)
print(content)

content=file.read(3) #print 3 char in line of file
print(content)

content=file.readline() #print whole line
print(content)

content=file.readlines() #print all lines in file
print(content)"""

file.close()

#tut 26- modes of file
#tut27 - solution of excersise 3