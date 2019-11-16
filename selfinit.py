class Employee:
    no_of_leaves=8

    def __init__(self,aname,asal):
        self.name=aname
        self.salary=asal


    def printdetails(self):
        return f"Name is {self.name}, {self.salary}"




Harry = Employee("Harry","455")
# Rohan = Employee()
print(Harry.name)

# Harry.name="Harry"
# Harry.salary=455
# # Harry.no_of_leaves=9
#
# Rohan.name="Rohan"
# Rohan.salary=4544

# print(Harry.no_of_leaves)
# print(Rohan.name)
# print(Harry.__dict__)

# print(Rohan.printdetails())