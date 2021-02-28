print(type("Hi hello my friend"))
# -------

long_string = '''
WOW
O O
---
'''
print(long_string)

# -------

first_name = 'Gustavo'
last_name = 'Lima'
full_name = first_name + ' ' + last_name

print(full_name)

# -------

# \t = TAB
# \n = ENTER
# \ = After the Back slash, will be turn in string

weather = "\n\tIt\'s \"kind of \" sunny \nhope you have a good day!\n"
print(weather)

# -------

# formatted strings

name = 'Gustavo'
age = 23

print('Hi ' + name + '.\nYou are ' + str(age) + 'yerars old')
# OR
# This is the recommended best format
print(f'Hi {name}. You are {age} years old')
# OR
print('Hi {}. You are {} years old'.format(name, age))
# OR

selfish = '01234567879'
# [start:stop:stepover]

print(selfish[5])
print(selfish[2:4]) # start at 2 and stop at 4, result = 2 and 3. 23
print(selfish[:5]) # start at 0 and stop at 5
print(selfish[:9:2]) # start at 0, stop at 9, and jump 2 numbers
print(selfish[::-1]) # the result is Reverse, When we use minus (-), its for reverse
