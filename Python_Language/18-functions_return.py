# using return - to return values
# this functions will return a sum of two numbers

def sum(num1, num2, num3):
    return num2 + num3


total = sum(100, 50, 50)
total2 = sum(10, 20, 30)

print(total, '\n')
print(total2)

# Return:
# Should do one thing really well.
# Should return something.


# comment functions
# create a funcion and give it a good comment
def animals(animal_1, animal_2):
    '''
    This is the animal function.
    '''
    print(f'\nI love to take care of my {animal_1}, and I have afraid of {animal_2}')


animals('Dog', 'Tiger')

# hel(), will help u with the function
# help(animals)
# OR
# print(animals.__doc__)
# this will help u with the function


def even(num1):
    '''
    This function will discover a even or odd number
    '''
    if num1 % 2 == 0:
        print('This is a even number')
    else:
        print('This is a odd number')
    return num1


even(90)

print(animals.__doc__)
print(even.__doc__)
