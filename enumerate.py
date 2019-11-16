l1=["Bhindi","aloo","chopsticks","chocks"]

# i=1
# for items in l1:
#     if i%2 is not 0:
#         print(f"please buy {items}")
#     i+=1

for index, item in enumerate(l1):
    if index % 2==0:
        print(item)