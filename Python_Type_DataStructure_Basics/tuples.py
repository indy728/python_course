# tuples are immutable
t = (1, 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))

t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))
