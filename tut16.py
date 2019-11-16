#for loop

list1=[[1,"abc"],[2,"pqr"],[5,"xyz"],[7,"wxy"]]
dict2=dict(list1)
for item,name in dict2.items():  #here .items() function is necessary oterwise rises error
    print(item,name)

#for item in list1:
 #   print(item,end=" ")

print("--------------------------------------")

dict1 = {"Harry":"burger",
         "Marrie":"pizza",
         "Carry":"jamun"}

for item in dict1:
    print(item)
    

for item in dict1.values():
    print(item)

print("--------------------------------------")

S1=set([1,2,3,4,5])

for item in S1:
    if(item==2):
        S1.add(22)
        S1.remove(2)
        continue
        print(S1)
    #print(item)

print("--------------------------------------")

items=[1,2,5,7,"Harry","AZ",13]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)