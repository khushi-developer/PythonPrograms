import json

data = '{"var1":"harry", "var2":56}'

parsed=json.loads(data)
print(parsed)
print(parsed['var1'])

# task1 - json.load

data2 = {
    "channe_name" : "codewithharry",
    "cars" : "audi ,Bmw",
     "fridge":"roti",
    "isbad":False
}

jscomp = json.dumps(data2)
print(jscomp)
print(data2["fridge"])

# task2- what is sort key parameter in dumps