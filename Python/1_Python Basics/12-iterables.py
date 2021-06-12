# ITERABLES

# iterable - list, dictionary, tuple, set, string

# iterate -> one by one check each item in the collection.


# let's create a Golem, with 5006 years old, that don't know how to swim
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# creating a loop that show the Keys
for my_loop in user:
    print(my_loop)

print('\n')

# OR using .keys() to show the keys
for my_loop in user.keys():
    print(my_loop)

print('\n')

# using .items() to show all the information of my dictionary
for my_loop in user.items():
    print(my_loop)

print('\n')

# using .values() to show the Value of my dictionary
for my_loop in user.values():
    print(my_loop)

print('\n')

# SUPER POWERFUL thing to know
for key, value in user.items():
    print(key, '    ', value)
