# # Lists
# name_user = ['James Bond', 'Robert Kiyosaki', 'Gustavo Lima', 'Jacob Harper']
# age_user = [55, 23, 56, 24, 80]
# cities_user = ['Campinas', 'Korea', 'New York']
#
# # Dictionary
# # Fist
# my_dict = {
#     'name': f'{name_user[2]}',
#     'age': f'{age_user[1]}',
#     'city': f'{cities_user[0]}'
# }
#
# person1 = {
#     'name': f'{name_user[0]}',
#     'age': f'{age_user[0]}',
#     'city': f'{cities_user[2]}'
# }
#
# print(person1.values())
#
# print(my_dict)
#
#
# # OOP
#
# class PlayerCharacter:
#     # Class Object Attribute
#     membership = True
#
#     def __init__(self, name, age):
#         self.name = name  # Attribute
#         self.age = age
#
#     def shout(self):
#         print('My name is ')
#
#
# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
#
# print(player1.shout(), player1.name, player1.age)
# print(player2.shout())
#
# print('\n')
#
# player2 = PlayerCharacter('Jayson', 50)
#
# print(player2.shout())
#
# # Exercise
#
# # Get the first character of the string txt
#
# txt = 'Hello World'
#
# x = txt[0]
# z = txt[2:5]
#
# print(x)
# print(z)
#
# # Return the string without any
# # whitespace at the beginning or the end.
# txt2 = "   Hello World   "
#
# print(txt2)
# print(txt2.strip())
# # strip()
#
# # Replace the character H with a J.
# txt3 = "Hellooo World"
# txt3 = txt3.replace('H', 'J')
# print(txt3)
#
# # ------------=-------------
#
# # SET exercise
#
# # Use the correct method to add multiple items (more_fruits) to the fruits set.
#
# fruits = {'apple', 'banana', 'cherry'}
# more_fruits = ['orange', 'mango', 'grapes']
#
# print(fruits, more_fruits)
#
# fruits.update(more_fruits)
# print('\n', fruits)
#
# # DICT exercises
#
# # Use the get method to print the value of the "model" key of the car dictionary.
#
# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
#
# print(car)
#
# print(car.get('model'))
#
# # Change the "year" value from 1964 to 2020.
#
# car['year'] = 2020
# print(car)
#
# # Add the key/value pair "color" : "red" to the car dictionary.
#
# car['color'] = 'red'
# print(car)
#
# # Add the key/value pair "color" : "red" to the car dictionary.
#
# car.pop('model')
# print(car)
#
# # Use the clear method to empty the car dictionary.
#
# car.clear()
# print(car)
#
# # If...Else - Exercises
#
# # find duplicates number - output: 2
#
# my_list = [1, 3, 4, 2, 2]
#
# duplicates = []
# for item in my_list:
#     if my_list.count(item) > 1:
#         if item not in duplicates:
#             duplicates.append(item)
#
# print(duplicates)

#
# #find duplicates
#
# list = [1,2,2,3,4,5,6,7,8,9,9]
#
# number = []
#
# for item in list:
#     if list.count(item) > 1:
#         if item not in number:
#             number.append(item)
#
# print(number)

# # ---------------------
#
# points = [1,4,2,9,7,8,9,3,1]
#
# number = []
#
# for i in points:
#     if points.count(i) > 1:
#         if i not in number:
#             number.append(i)
#
# print(number)
