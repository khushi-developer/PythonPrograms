#set
s=set()
print(type(s))

l=[1,2,3,4]
s1=set(l)
#print(s1)

#s1.update([33])
#print(s1)

#s1.add(5)
#s1.add(5)#set add one element only one time
s2 = s1.union([1,6])
s2=max(s1)
s2=min(s1)
print(len(s1))
s2 = s1.intersection([1,3,9])
s2=s1.isdisjoint(s)
print(s2)
