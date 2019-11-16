class A:
    def prit1(self):
        print("This is A")

class B(A):
    def prit1(self):
        print("This is B")


class C(A):
    def prit1(self):
        print("This is C")


class D(B,C):
    def prit1(self):
        print("This is D")


a=A()
b=B()
c=C()
d=D()

print(a.prit1())
print(d.prit1())