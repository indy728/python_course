def myfunc(a,b):
    # returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))

def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(1))
print(myfunc(1,50,90,44,234,5))
print(myfunc(1,2,3,4,5,6))

def myfunc(**kwargs):
    if 'chow' in kwargs:
        print(f"I eat {kwargs['chow']}")
    elif 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("Ain't no fruit here")

myfunc(fruit = 'apple', veggie = 'celery', chow = 'beats')

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}.")

myfunc(3,6,9,fruit = 'apple', veggie = 'celery', food = 'beats')