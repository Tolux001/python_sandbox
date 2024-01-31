# A List is a collection which is ordered and changeable. Allows duplicate members.

# Creating List(Or Array as know in js)

# Straight forward Method
numbers = [1, 2, 3, 4, 5]

# Using constructors
number2 = list((1, 2, 3, 4, 5))

print(numbers, number2)

# Fruit list
fruits = ['Orange', 'Apple', 'Banana', 'Pear']

first_fruit = fruits[1]
print(first_fruit)

length_of_fruit = len(fruits)
print(length_of_fruit)

# To add and Remove
fruits.append('Mangoes')
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.insert(2, 'Walnut')
print(fruits)

fruits.pop(3)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits[0] = "BlueBerry"
print(fruits)
