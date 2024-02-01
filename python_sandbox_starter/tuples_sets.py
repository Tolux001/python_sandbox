# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Creating tuples : Another way odf creating *list* but doesn't have a lot of functions like *list* and it's unchangeable
fruits = ("Apple", "Pineapple", "Orange", "Grape")
print(fruits)

# Always remember to use comma after a single value  
fruits3 = ("Boats")
print(fruits3, type(fruits3))

fruits2 = ("Boats",)
print(fruits2, type(fruits2))

# A Set is a collection which is unordered and un-indexed. No duplicate members.
fruit_set = {'Apples', 'Orange', 'Mangoes'}

print(fruit_set)

findStr = 'Apples' in fruit_set
print(findStr)

findStr = fruit_set.add('Grape')
print(fruit_set)

findStr = fruit_set.remove('Orange')
print(fruit_set)

fruit_set.clear()
print(fruit_set)

del fruit_set

