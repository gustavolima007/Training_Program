# functions

def image_one():
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


image_one()
image_one()

# parameters


def informations(name, age, city):
    print(f'Hello {name}, do you have {age} years old and live in {city} city.')


# arguments
informations('Gustavo Lima', '22', 'SP')
informations('Lima', '25', 'WA')
# positional argumets
informations('James Bond', '45', 'NY')
# keyword arguments
informations(age=16, city='NY', name='Sherk')
informations(name='Sherk', age=16, city='NY')  # this is better
