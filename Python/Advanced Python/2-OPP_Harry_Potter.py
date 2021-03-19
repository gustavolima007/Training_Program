# OOP
# Self
# Create a class for the Harry Potter Character's

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


# Instantiate
player1 = PlayerCharacter('Hermione Granger', 22)
player2 = PlayerCharacter('Ronald Weasley', 23)

print(player1.name, player1.age)  # this will print the name and age of player1
print(player2.name, player2.age)

print('\n')

print(player1, player2)  # this will show the memory location

print('\n')

print(player2.run())  # this will print and return the function of run()

print('\n')

help(player2)