# syntax of for loops:
exhibit_a = [1, 2, 3]

for number in exhibit_a:
    print(number * 4)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    if (not num % 2):
        print ("Even number: {}".format(num))
    else:
        print ("Odd number: {}".format(num))

list_sum = 0

for num in my_list:
    list_sum += num
print(list_sum)

for _ in ('Hello World'):
    print('This is convention for a variable name that isn\'t used!')

tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

print("tuple_list: {}".format(tuple_list))
for a, b in tuple_list:
    print("a = {a} and b = {b}".format(a=a, b=b))

# looping through a dictionary
d = {'k1':1,'k2':2, 'k3':3}

for item in d:
    print(item)

for item in d.items():
    print(item)

# while loops are similar syntax
x = 0

while x < 5:
    print("The current value of x is: {}".format(x))
    x += 1
# while loops can also have else statements
else:
    print("END LOOP BEEP BOOP")

my_name = "Alexis"
for letter in my_name:
    if letter == 'x':
        continue
    print(letter)