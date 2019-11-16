#seek nd tell

file=open("khushi.txt","r")
contents=file.read(8)
a=file.tell()
print(a)
file.seek(40)
contents=file.read()
print(contents)
file.close()