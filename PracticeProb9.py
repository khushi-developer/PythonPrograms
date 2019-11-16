#funny names

import random
num = int(input("Enter the number of names:"))
counter = num
print(f"Enter the {num} space separated names")
names=[]
while num:
    names.append(input())
    num-=1

f_individual_list=[]
l_individual_list=[]
for name in names:
    first_name=name.split(" ",0)
    last_name = name.split(" ",1)
    f_individual_list.append(first_name)
    l_individual_list.append(last_name)
    print(f_individual_list,l_individual_list)

funny_names=[]
while counter:
    f=random.choice(f_individual_list)
    l=random.choice(l_individual_list)

    f_individual_list.remove(f)
    l_individual_list.remove(l)
    funny_names.append(f+''+l)
    counter-=1

print(funny_names)