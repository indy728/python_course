myfile = open('test.txt')
# myfile = open('test2.txt')
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
contents = myfile.read()
print("contents: " + contents)
myfile.close()
with open('test.txt') as my_new_file:
    new_contents = my_new_file.read()
print(new_contents)

with open('test.txt', mode='a') as my_file2:
    my_file2.write("turd sandwich")
last_file = open('test.txt')
print(last_file.read())
last_file.close()
# can create a new file with mode='w' for writeable