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


Harry=Employee("Harry",1,43)
Rohan=Employee("Rohan",2,34)

# print(Harry.printdetails())
# print(Harry.name)
#
# Rohan.change_leaves(11)
# print(Employee.no_of_leaves)