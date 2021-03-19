# show a list with 6 numbers, and sum just the even numbers
# example: 1, 2, 3, 4, 5, 6 - Result = 12

numbers = list(range(0, 7, 2))

i = 0
counter = 0

for i in numbers:
    i += i
    counter += 1
print(f'All the sum of the {counter} even numbers are: {i}')
