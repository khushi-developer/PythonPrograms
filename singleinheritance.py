class Employee:
    no_of_leaves=8

    def __init__(self,aname,asection,aroll):
        self.name=aname
        self.section=asection
        self.roll=aroll

    def printdetails(self):
        return f"This is name {self.name}, {self.section},{self.roll}"

    @classmethod
    def change_leaves(cls,newleves):
        cls.no_of_leaves=newleves


class programmer(Employee):
    no_of_holiday=56

    def __init__(self,aname,asection,aroll,languages):
        self.name = aname
        self.section = asection
        self.roll = aroll
        self.languages=languages

    def printprog(self):
        return f"the name of programer{self.name},{self.section},{self.roll} ,{self.languages}"



Harry=Employee("Harry",1,43)
Rohan=Employee("Rohan",2,34)
dev=programmer("dev",3,455,"python")
karan=programmer("reva",4,777,["python","java"])

print(karan.no_of_holiday)
print(karan.printprog())