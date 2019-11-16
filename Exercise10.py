# pickelling iris database

import pickle
import requests
data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/").text
# print(data)

l1=data.split("\n")
# print(l1)
l2=[item.split(",") for item in l1 if len(item)!=0]
print(l2)

# write on to file by pickle
fileobj=open("myfile1.txt","wb")
pickle.dump(l2,fileobj)
fileobj.close()

# to read this pickle
fileobj = open("myfile1.txt",'rb')
mydata=pickle.load(fileobj)
print(mydata)