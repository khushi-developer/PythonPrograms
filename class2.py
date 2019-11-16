class Employee:
    no_of_leaves=10
    pass

Harry = Employee()
Rohan = Employee()

Harry.name="Harry"
Harry.salary=455
Harry.no_of_leaves=9

Rohan.name="Rohan"
Rohan.salary=4544

print(Harry.no_of_leaves)
# print(Rohan.name)
print(Harry.__dict__)
print(Employee.__dict__)