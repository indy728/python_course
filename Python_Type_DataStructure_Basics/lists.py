# lists are indexed and can be sliced and can hold any variety of data types
my_list = [1, 2, 3]
print(len(my_list))
print(my_list[1:])
next_list = [4, 5, 6]
double_list = my_list + next_list
print(my_list + next_list)
print(double_list)
# lists are mutable
double_list[4] = "turd sandwich"
print(double_list)
double_list.append(7)
print(double_list)
print(double_list.pop(-3))
print(double_list)
double_list.reverse()
print(double_list)

