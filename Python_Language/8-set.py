# set - is an unordered collection of unique objects

my_set = {1, 2, 3, 4, 5, 5}
print(my_set)

print('\n')

my_set.add(100)
my_set.add(2)
print(my_set)

print('\n')

print(len(my_set))

print('\n')


# Set Methods

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()  -  nothing in common
# .issubset()
# .issuperset()
# .union()   -   united the set together

set_example = {1, 2, 3, 4, 5}
set_example2 = {1, 2, 3, 4, 5}
set_example3 = {4, 5}

your_set = {4, 5, 6, 7, 8, 9, 10}

print(set_example.difference(your_set))
print('\n')

set_example.discard(5)
print(set_example)
print('\n')

set_example.difference_update(your_set)
print(set_example)
print('\n')

print(set_example2.intersection(your_set))
print('\n')

print(set_example2.isdisjoint(your_set))  # nothin in common, so is false
print('\n')

print(set_example2.union(your_set))
print('\n')

print(set_example3.issubset(your_set))

print(set_example3.issuperset(your_set))
