# Do a list 0 to 500, with just the odd number, and then sum all multiples of 3

# end=' ' - to create a list

sum = 0
counter = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        counter += 1
        sum += i
print(f'The sum of all the {counter} values is: {sum}!')
