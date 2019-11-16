grocery = ["harpic","bhindi","loollypop"]
print(grocery[0:2])
numbers = [2,1,3,5,1,9,7]
numbers.remove(5)
numbers.pop(2)
numbers.sort()
c=numbers.count(1)
numbers.append(3)
numbers.append(3)
numbers.reverse()
numbers.insert(2,13)
print(numbers)

print("---------------------------------------------------------")

#list can be mutable(can change)
#tuple immutable (cannot change)

tp = (1,3,5)
print(tp)

a=2
b=6
a,b=b,a #swapping can do directly
print(a,b)