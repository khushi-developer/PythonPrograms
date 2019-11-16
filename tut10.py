#dictionary is nothing but key value pairs
d1 = {}
print(type(d1))

d2 = {"khushi":{"B":"vada pav,samosa","L":"kofta","D":"pulav"},
      "reva":"samosa",
      "vedu":"pav bhaji"}
print(d2["reva"])
print(d2["khushi"]["B"])

d2["aniket"]="junk food"
print(d2) #or u can write this
d2.update({"leena":"Toffee"})
print(d2)
del d2["aniket"]
print(d2)

d3=d2.copy()
del d3["khushi"]
print(d3)

print(d2.keys())
print(d2.items())
print(d2.values())


