# link to study? https://www.w3schools.com/python/python_ref_keywords.asp

basket = ['a', 'd', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d'))  # 3th position
print('d' in basket)  # True or False?
print('x' in basket)
print('i' in 'Hi my name is Gustavo')

print(basket.count('d'))  # how many 'd' exist in the list?

print('\n')

# How to put in sequence using sort. or sorted()
basket2 = ['a', 'x', 'd', 'b', 'c', 'd', 'e', 'c', 'z', 'd']
# basket2.sort()

print(sorted(basket2))

print('\n')

# reverse lists
basket2.sort()
basket2.reverse()
print(basket2)

print('\n')

# reverse list with [::-1]
print(basket2[::-1])
print(basket2)

print('\n')

# printing a list of numbers
print(list(range(-10, 200)))

print('\n')

# using join. to put information in space between the words
sentence = '1'
new_sentence = sentence.join(['Hi', 'My', 'Name', 'is', 'Gustavo', 'Lima'])
print(new_sentence)
# OR
new_sentence2 = '   '.join(['Hi', 'My', 'Name', 'is', 'Gustavo', 'Lima'])
print(new_sentence2)
