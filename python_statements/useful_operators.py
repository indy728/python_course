# range
for num in range(-5, 50, 3):
    print(num)

# cast range as an object:
range_to_list = list(range(-5, 50, 3))
print(range_to_list)

# enumerate
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

for item in enumerate('abcde'):
    print(item)

my_list1 = list(range(0, 5))
my_list2 = list(range(5, 10))

# zip will only pair lists to the length of the shortest list
for item in zip(my_list1, my_list2):
    print(item)

print('6' in my_list2)
print(6 in my_list2)

# libraries
from random import shuffle

my_list = list(range(1,100))
shuffle(my_list)
print(my_list)
shuffle(my_list)
print(my_list)
my_list.sort()
print(my_list)

from random import randint
print(randint(0,100))
print(randint(0,100))

# user input
user = raw_input("What's your name, bitch? ")
# print(user)
print("This bitch's name is {}".format(user))