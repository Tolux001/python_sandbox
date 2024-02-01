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

