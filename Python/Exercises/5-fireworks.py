# Fireworks Exercise

import time

fireworks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in fireworks[::-1]:
    time.sleep(1)
    print('\n', i)

print('\nBOOOM!!!\n')

image_fireworks = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0]
]

for line in image_fireworks:
    for pixel in line:
        if (pixel == 0):
            print(' ', end='')
        elif (pixel == 1):
            print('*', end='')
        else:
            print('@', end='')
    print('')

print("\nHappy New Year, Folks!\nLet's drink!!!\n")
