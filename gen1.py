def gen(n):
    for i in range(n):
        yield i

g= gen(3)
print(g)
# print(g.__next__())

for i in g:
    print(i)


h="abc"
iter=iter(h)
print(iter.__next__())

for c in h:
    print(c)
    