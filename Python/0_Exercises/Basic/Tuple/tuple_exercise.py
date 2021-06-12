print('1. Write a Python program to create a tuple.\n')

tuple1 = (1, 2, 3, 4, 5, 6)

print(tuple1)
# OR
typlex = tuple()

print(typlex, '\n')

print('2. Write a Python program to create a tuple with different data types.\n')

tuple2 = ('yeah baby', 1, 2, False, 5.7)

print(tuple2, '\n')

print('3. Write a Python program to create a tuple with numbers and print one item.\n')

my_tuple = (1, 2, 3, 4, 5)

x = my_tuple.index(3)

print(x)
# OR
print(my_tuple.index(4), '\n')

print('4. Write a Python program to unpack a tuple in several variables.\n')

tup = (1, 2, 3, 4, 5, 6)

n1, n2, n3, n4, n5, n6 = tup

print(n1 + n2 + n3 + n4 + n5 + n6, '\n')

print('5. Write a Python program to add an item in a tuple.\n')

tuplex = (1, 2, 3)

n4 = (4,)
n5 = (5, 6, 7, 8, 9, 10)

tuplex = (555,) + tuplex + n5 + n4 + (555,)

print(tuplex, '\n')

# adding items in a specific index

tuplex = tuplex[:7] + (15, 20, 25) + tuplex[:3]

print(tuplex, '\n')

print('6. Write a Python program to convert a tuple to a string.\n')

tuple7 = ('123', '123', '123')

str = '*'.join(tuple7)

print(str, '\n')

print('7. Write a Python program to get the first element and last element from last of a tuple.\n')

tupx = ('Jackson Ville', False, True, 1, 2, 6, 'New York')

first_element = tupx[0]
last_element = tupx[6]

print(f'The First element of the Tuple is: {first_element}\nAnd the last element is: {last_element}\n')
