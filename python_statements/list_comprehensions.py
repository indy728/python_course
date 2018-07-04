mylist = []
mylist2 = [letter for letter in 'yogi']

for letter in 'whores':
    mylist.append(letter)

print(mylist)
print(mylist2)

range1 = [num for num in range(1, 11)]
range2 = [num * 2 for num in range(1, 11)]
range3 = [num ** 2 for num in range(1, 11)]
print(range1)
print(range2)
print(range3)

even = [x for x in range(1, 11) if not x % 2]
print(even)

celcius = [0.0, 10.0, 20.0, 34.5]
fahrenheit = [temp * 9 / 5 + 32 for temp in celcius]

# fahrenheit = []
# for temp in celcius:
#     fahrenheit.append(temp * 9 / 5 + 32)

print(fahrenheit)

