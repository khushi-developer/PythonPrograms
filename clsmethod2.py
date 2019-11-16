class Employee:
    def __init__(self,aname,asection,aroll):
        self.name=aname
        self.section=asection
        self.roll=aroll

    def printdetails(self):
        return f"This is name {self.name}, {self.section},{self.roll}"

    @classmethod
    def from_dash(cls,string):
        params=string.split("-")
        return cls(params[0],params[1],params[2])
        # return cls(*string.split("-"))



karan=Employee.from_dash("karan-1-23")
print(karan.printdetails())

