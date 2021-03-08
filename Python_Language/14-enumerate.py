# Enumerate

# Char = character
# String
for i, char in enumerate('Helllooo'):
    print(i, char)

print('\n')

# Numbers int
for i, char in enumerate((1, 2, 3, 4, 5)):
    print(i, char)

print('\n')

# How to find the 50 position value
for i, char in enumerate(list(range(60))):
    if char == 50:
        print(f'Index of 50 is: {i}')

print('\n')
