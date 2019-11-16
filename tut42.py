import time
initial=time.time()
print(initial)

n=3
for i in range(n):
    print("*")
    time.sleep(2)
print(time.time()-initial)


initial2=time.time()
k=0
while(k<3):
    print("*")
    k+=1
print(time.time()-initial2)

Localtime=time.asctime(time.localtime(time.time()))
print(Localtime)