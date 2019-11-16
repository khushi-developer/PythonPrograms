class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def printdetails(self):
        return f"This is {self.name} and {self.sal}"

    def __add__(self, other):
        return self.sal+other.sal

    def __truediv__(self, other):
        return self.sal / other.sal

    def __mul__(self, other):
        return self.sal*other.sal

    def __repr__(self):
        return  f"This is ('{self.name}' and {self.sal})"

    def __str__(self):
        return f"This is {self.name} and {self.sal}"

Harry=Employee("Harry",455)
Rohan=Employee("Rohan",55)

print(Harry+Rohan)
print(Harry / Rohan)
print(Harry*Rohan)

print(Harry)
print(repr(Harry))