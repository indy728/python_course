# 1: print Hello World

def myfunc():
    print('Hello World')


myfunc()


# 2: print Hello Name

def myfunc(name):
    # print(f"Hello is {name}")
    print("Hello {}".format(name))


myfunc("Jose")


# 3: simple Boolean

def myfunc(a):
    return 'Hello' if a == True else 'Goodbye'


print(myfunc(True))
print(myfunc(False))


# 4: using Booleans

def myfunc(x, y, z):
    return x if z == True else y


print(myfunc(42, 69, 3 < 4))
print(myfunc(42, 69, 3 > 4))


# 5: Simple Math

def myfunc(a, b):
    return a + b


print(myfunc(4, 7))


# 6: Is Even

def is_even(n):
    return True if not n % 2 else False


print(is_even(42))
print(is_even(69))


# 7: Is Greater

def is_greater(a, b):
    return True if a > b else False


print(is_greater(3, 4))
print(is_greater(3, 2))


# 8: *args

def myfunc(*args):
    return (sum(args))


print(myfunc(1, 2, 3, 4))


# 9: pick evens

def myfunc(*args):
    return [num for num in args if not num % 2]


print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9))


# 10: skyline

def myfunc(string):
    newstring = ""
    for num, char in enumerate(string):
        char = char.lower() if num % 2 else char.upper()
        newstring += char
    return newstring


print(myfunc("Mississippi"))


# GITHUB PRACTICE
## SPY GAME

# def spy_game(numbers):
#     mylist = []
#     for num in numbers:
#         if ((len(mylist) == 0 or len(mylist) == 1) and num == 0) or \
#                 (len(mylist) == 2 and num == 7):
#             mylist.append(num)
#         if mylist == [0, 0, 7]:
#             return True
#     return False

def spy_game(numbers):
    code = [0,0,7,'x']
    for num in numbers:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

## COUNT PRIMES

# def count_primes(number):
#     x = 3
#     count = 0 if number < 2 else 1
#     while x <= number:
#         y = 2
#         while y <= x / 2:
#             if not x % y:
#                 break
#             y += 1
#         if y >= x / 2 and x % y:
#             count += 1
#         x += 2
#     return count

def count_primes(number):
    x = 3
    count = 0 if number < 2 else 1
    while x <= number:
        for y in range (3, x, 2):
            if not x % y:
                break
        else:
            count += 1
        x += 2
    return count

print(count_primes(100))
print(count_primes(21))
print(count_primes(-4))
