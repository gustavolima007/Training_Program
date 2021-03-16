def highest_even(li):
    '''
    This function will print the highest even number
    '''
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even.__doc__)

print(highest_even([10, 2, 3, 4, 8, 11]))
