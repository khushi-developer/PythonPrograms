# file=open("khushi.txt","w")
# a=file.write("This is me")
# print(a)
# file.close()

# file=open("khushi.txt","a")
# file.write("This is me\n")
# file.close()

#open for both read and write operayion

file=open("khushi.txt","r+")
file.write("Ha mai bhi hu")
content=file.read(33333)
print(content)
file.close()