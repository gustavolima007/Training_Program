# lists
# Data Structure
# Python List/Array Methods - https://www.w3schools.com/python/python_ref_list.asp

amazon_cart = ['Notebooks', 'Sunglasses', 'Books', 'Toys']
print('Your first and last itens on Amazon:\n', amazon_cart[0])
print(amazon_cart[2], '\n')

# list slicing
amazon_cart[3] = 'Laptop' # this will change the item on my first list

new_cart = amazon_cart[:] # use [:], to copy the list

new_cart[0] = 'Fire Gum' # this will change the item on my new list

print(amazon_cart, '\n') # first list
print(new_cart, '\n') # new list


# Matrix - How to take just the number 5?
matrix = [
    [1, 5, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 0]
]
print(matrix[0] [1], '\n')

# append
matrix.append([100, 50, 10]) # add more information to the list
print(matrix, '\n')

# insert - to modify
new_list = [1, 2, 3, 5, 8]
print(new_list)

new_list.insert(3, 4) # to add information in a specific position of the list
print(new_list)

# extend - to add more information
new_list.extend([20, 30, 40])
print(new_list, '\n')

# remove to the list
new_list.pop(5) # look here
print(new_list, '\n')
# OR
new_list.remove(30) # look here
print(new_list, '\n')
# OR - use Clear to remove all
new_list.clear()
print(new_list)

# What I have learn in this section
#1 - basket.remove('Banana')
#2 - basket.pop()
#3 - basket.append('Kiwi')
#4 - basket.insert(0, 'Apples')
#5 - basket.count('Apples')
#6 - basket.clear()
