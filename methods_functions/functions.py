# syntax of functions
def name_of_function(name):
    """
    Docstring explains function, accessible from help function. Explanation of inputs and output are helpful
    """
    print("hello " + name)


name_of_function("Kyle")


def addition(num1, num2):
    return num1 + num2


sum = addition(4, 7)
longstring = addition("turd ", "sandwich")

print(f"sum is {sum} and longstring is {longstring}")


def say_hello(name='user'):
    print("hello " + name)


say_hello()
say_hello('Farty')


# Find out if the word "dog" is in a string
def dog_check(is_dog):
    return 'dog' in is_dog.lower()


print(dog_check('Dog is uppers and lowers'))
print(dog_check('Bog is uppers and lowers'))


# pig latin function
def pig_latin(pig_word):
    if pig_word[0].lower() in 'aeiou':
        return pig_word + ("ay" if not pig_word[-1] == 'a' else "y")
    else:
        vowel_index = get_vowel_index(pig_word)
        return pig_word[vowel_index:] + pig_word[:vowel_index] + ("ay" if not pig_word[-1] == 'a' else "y")


def get_vowel_index(word):
    for index, char in enumerate(word):
        if char in 'aeiou':
            return index
    raise ValueError("No vowel found")

print(pig_latin("scram"))
print(pig_latin("America"))
