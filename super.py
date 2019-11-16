class A:
    classvar1="I m in class A"
    def __init__(self):
        self.classvar1="I m instance var in class A"
        self.var1="I m var1 in class A"
        self.special="special"

class B(A):
    classvar1="I m class var in class B"
    def __init__(self):
        super().__init__()
        self.classvar1="I m instance var in class B"
        self.var1="I m var1 in class B"
        print(super().classvar1)
a=A()
b=B()

print(b.special,b.classvar1,b.var1)