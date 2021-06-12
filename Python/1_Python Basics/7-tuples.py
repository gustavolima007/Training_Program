# tuple (less flexible of a list, but you can't modify a tuple. It's immutable)
# we create tuple to not change
# tuple has two methods that we use
#   count()
#   index()

my_tuple = (1, 2, 3, 4, 5, 5, 5)

print(my_tuple[1])

print('\n')

print(3 in my_tuple)

print('\n')

print(my_tuple.count(5))
# count() - its will count the among of numbers

print('\n')

print(my_tuple.index(5))
# index - will count after 0. (0, 1, 2, 3, 4)

print('\n')

print(len(my_tuple))
# len - will count all the keys

print('\n')
