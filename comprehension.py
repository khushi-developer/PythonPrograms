# ls=[i for i in range(100) if i%2==0]
# print(ls)

# dict1={i: f"item{i} " for i in range(10) if i%2==0}
# print(dict1)
#
# dict2={value:key for key, value in dict1.items()}
# print(dict2)

# dresses={dress for dress in["dress1","dress2",
#                             "dress1","dress2"] }
# print(dresses)

gen=(i for i in range(10))
# print(gen.__next__())

for item in gen:
    print(gen.__next__())