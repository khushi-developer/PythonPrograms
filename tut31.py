#with block , using this we can exclude the file open nd close operation, it is same as file open close operation

with open("khushi.txt","r") as f:
    a=f.read()
    print(a)

f=open("khushi.txt","r")
c=f.read(4)
print(c)