class Employee:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def printdetails(self):
        return f"This is {self.name} and {self.roll}"

    @staticmethod
    def printstr(string):
        return f"this is string {string}"



Harry=Employee("Harry",1)
Rohan=Employee("Rohan",2)

print(Harry.printdetails())

print(Employee.printstr("Ram"))