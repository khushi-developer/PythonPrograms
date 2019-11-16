# ls1=['1','4','3','9','7']
ls1 = [1, 4, 3, 9, 7, 3, 5]
# ls1.reverse()
# print(ls1,"\n")

print(ls1[::-1],"\n")

j=len(ls1)-1
i=0
p=j/2

def swapPosition(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

for item in ls1:
    print(swapPosition(ls1,i,j))
    i+=1
    j-=1

    if i==p:
        break