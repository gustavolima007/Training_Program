print('\nExercise 1: Print First 10 natural numbers using while loop\n')

i = 0

while i < 10:
    i += 1
    print(i)

print('\nExercise 2: Print the following pattern\n')
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

lastNumber = 6

for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print('')

print('\nExercise 3: Accept number from user and calculate the sum of all '
      'number from 1 to a given number. For example, if user entered 10 the output should be 55.\n')

print('Put a number to calculate all the sum of them: ')
number = input()

i = 10
for i in number:
    i += i
    print(i)



print('\nExercise 4: Print multiplication table of a given number '
      'For example, num = 2 so the output should be\n')



print('\nExercise 5: Given a list, iterate it, and display numbers divisible by five, '
      'and if you find a number greater than 150, stop the loop iteration.\n')

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
