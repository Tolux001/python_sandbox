# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1 #int
# y = 2.5 #float
# dog_name = "Pulpy" #String
# is_cool = True #bool

# # multiply assignment
# x, y, dog_name, is_cool = (1, 2.5, "Pulpy", True)

# print("Hello world!")

# # basic math

# a = x + y

# print(a)

# # Knowing types

# variable_type = type(a)

# print(variable_type)

# # Casting: converting a num to other data types

# variable_type = type(str(a))

# # print(variable_type)

# a = 1
# b = 0.5
# c = "Toluwalase"

# a = str(a)
# a = float(a)

# print(type(a))

# Concatenation
name = "Peter"
age = 1

sentence_calling = "My name is " + name + " and I am " + str(age) + " year old." 
print(sentence_calling)

# or 

sentence_call = ('My name is {name} and I am {age} years old'.format(name=name, age=age))
print(sentence_call)

# or

sentence_calls = (f'My name is {name} and I am {age} years old')

print(sentence_calls)

# Strings Methods

cat_sound = "puRR"

print(cat_sound.capitalize())
print(cat_sound.upper())
print(cat_sound.lower())
print(cat_sound.swapcase())
print(cat_sound.replace('old_word', 'new_word'))
print(len(cat_sound))
print(cat_sound.count('character you want to count'))
print(cat_sound.endswith('d'))
# ...............................