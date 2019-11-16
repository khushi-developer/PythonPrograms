myvar = "khushi is a good girl"
print(myvar[0:5])
print(myvar[3:7])
print(myvar[-4:-2])


myvar = "khushi is a good girl"
print(myvar[0:5:2])#skip 1 char
print(myvar[0:10:3]) #skips 2 chars

myvar = "khushi is a good girl"
print(myvar[::]) #here by default 0th posn , total length of string , and 1 for slicing
print(myvar[ : :-1]) #reverse the string

print("-----------------------------------------")

print(len(myvar))
print(myvar.isalnum())
print(myvar.isalpha())
print(myvar.endswith("girl"))
print(myvar.count("o"))


print(myvar.capitalize())
print(myvar.upper())
print(myvar.lower())
print(myvar.replace("is","are"))
