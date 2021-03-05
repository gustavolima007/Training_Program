#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.

---------------------------------------------------------

#1
profile_user = {
    'age': 22,
    'username': 'Thor Ragnarok',
    'weapons': ['sword'],
    'is_active': True,
    'clan': ' '
}
#2 - this will print just the keys
print(profile_user.keys())

print('\n')

#3 - this will add a new key for weapons
profile_user['weapons'].append('shield')
print(profile_user)

print('\n')

#4
profile_user.update({'is_banned': False})
print(profile_user)

print('\n')

#5
profile_user.update({'is_banned': True})
print(profile_user)

print('\n')

#6
profile_user2 = profile_user.copy()
profile_user2.update({'age': 37})
profile_user2.update({'username': 'James Franco'})
print(profile_user2)
