mystring = "Hello World"
print(mystring[0])
print(mystring[-1])
newstring = "abcdefghijk"
print(newstring[2:])
print(newstring[:3])
print(newstring[3:8])
print(newstring[2::2])
print(newstring[8:2:-1])
# strings are immutable in python
name = "ham"
# name[0] = 'p'
newname = 'p' + name[1:]
print(newname)
hello = 'hello world'
hello = hello.capitalize()
print(hello)
split = hello.split()
print(split)
fstring = "This is a float: {1} and this is a string: '{0}'".format("I am a string", 3.2)
print(fstring)
print('her name is {}'.format(name))
