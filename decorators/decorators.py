def func():
    return 1

def hello():
    return "Hello!"

greet = hello

del hello
greet()

def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet function inside hello!'
    
    def welcome():
        return '\t This is welcome inside hello'
    
    # print (greet())
    # print(welcome())
    # print ('this is the end of the hello function')
    print('I am going to return a function')
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello("kyle")
print(my_new_func())

def hello():
    return 'Hi Kyle'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)

def new_decorator(orig_func):

    def wrap_func():

        print('Some extra code before the original function')

        orig_func()

        print('Some extra code after the original function')
    
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

decorated_function = new_decorator(func_needs_decorator)
decorated_function()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()