class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@khushikaprogram.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@khushikaprogram.com"

    @email.setter
    def email(self,string):
        print("setting now.....")
        names = string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

Khushi=Employee("khushi","padadune")

# print(Khushi.explain())
print(Khushi.email)

Khushi.fname="dea"
print(Khushi.email)

Khushi.email="this.that.@gmail.com"
print(Khushi.email)

del Khushi.email
print(Khushi.email)

print("========================tut70==============================")

print(type(Khushi))
print(id(Khushi))
o="this is string "
print(dir(o))
print(dir(Khushi))

import inspect
print(inspect.getmembers(Khushi))