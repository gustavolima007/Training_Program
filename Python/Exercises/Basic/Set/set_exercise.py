print('1. Write a Python program to create a set.\n')

set1 = {1, 2, 3, 4, 5, 6}
print(set1)
x = {1, 2, 3, 4, 5, 6}
print(x)

print('2. Write a Python program to iterate over sets.\n')

setx = {1, 2, 3, 4, 5, 6}

for i in setx:
    print(i)

print('3. Write a Python program to add member(s) in a set.\n')

members = {'Manoela', 'James', 'Lima'}
members.add('Eleven')
print(members, '\n')

print('4. Write a Python program to remove item(s) from set.\n')

members2 = {'Manoela', 'James', 'Lima'}
members2.remove('Manoela')
print(members2)

print('5. Write a Python program to remove an item from a set if it is present in the set.\n')

members3 = {'Manoela', 'James', 'Lima'}
members3.discard('Lima')
members3.discard('Shelby')
print(members3)

print('6. Write a Python program to add an item.\n')

setAB = {"a", "b"}

print(setAB.__doc__)

setAB.add('C')

print(setAB)
