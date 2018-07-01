# sets are unordered collections of unique elements
myset = set()
myset.add(1)
print(myset)
myset.add(2)
myset.add(2)
print(myset)
# casting a list to a set
# sets do not have an order
mylist = [1,2,2,1,1,1,2,3,4,3,3,4,5,5,4]
print(set(mylist))