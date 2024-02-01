# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Similar to object in JS

person = {
    'first_name' : 'Toluwalase',
    'last_name' : 'Adejuwon'
}
print(person, type(person))

university_colleges = {
    "colphys": 5,
    "Colbios": 10,
    'colaminin': 20,
    'Senate_building': "president & The vice & senate"
}

first_college = university_colleges["colphys"]
print(first_college)
print("I am going with", university_colleges['Senate_building'], "to the ceremonial building at ", university_colleges["colaminin"])


university_colleges['phone_number'] = '2349038358375'
print(university_colleges)

key_value = university_colleges.keys()
print(key_value)

item_value = university_colleges.items()
print(item_value)


copy_value = university_colleges.copy()
print(copy_value)
copy_value["add_value"] = "my_name_is_Toluwalase"
print(copy_value)
del(copy_value['Senate_building'])
print(copy_value)


# dictionaries length
print(len(university_colleges))
print(len(copy_value))

# Dictionary in List : Is the same thing with
    # Object in Array
dict_list = [
    {'name': 'Toluwalase', 'age': '12', 'color': "Blue"},
    {'name': 'Peter', 'age': '45', 'color': "Pink"},
    {'name': 'Sophia', 'age': '909', 'color': "White"},
]

first_dict_name = dict_list[0]['name']
print(first_dict_name)

