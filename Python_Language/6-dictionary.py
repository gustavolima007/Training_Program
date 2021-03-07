# list unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)

print('\n')

# none
weapons = None
print(weapons)

print('\n')

# dictionary
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}

print(dictionary['b'])

print('\n')

dictionary2 = {
    'a': [1, 2, 3, 4],
    'b': 'Hello',
    'x': True,
    'z': None
},            {
    'a': [1, 2, 3, 4, 55, 6, 7, 800],
    'b': 'Let\'s do it',
    'x': False,
    'z': None
}

print(dictionary2[1]['b'])
print(dictionary2[0]['x'])
print(dictionary2[1]['a'][4])

print('\n')

# dictionary using dict()
user2 = dict(name='JohnJohn', name2='LindaRobson')
print(user2)

print('\n')

# dictionary
user_info = {
    'age': [10, 20, 30],
    'name': 'Jack'
}
# user_info.clear() to clear all the dictionary
# user_info.copy() to copy a second dictionary
# user_info.pop() to remove a key and value of the dictionary
user_info.update({'name': 'Tompson'})
user_info.update({'age': 55})
print(user_info)
print(user_info.items())
