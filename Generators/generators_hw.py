# PROBLEM 1

def gensquares(n):

    for x in range(n):
        yield x**2

for x in gensquares(10):
    print(x)

print()

# PROBLEM 2

import random

def rand_int(low, high, n):

    for i in range(n):
        yield random.randint(low, high)

for num in rand_int(1,10,12):
    print(num)

print()

# PROBLEM 3

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print()

# PROBLEM 4

# Idk probably if you want to return many values but not keep those values in memory. Liiiike IDFK

# PROBLEM 5

