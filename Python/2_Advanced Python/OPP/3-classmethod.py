# OOP
# @classmethod
# @staticmethod

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# doest need to instantiate using the lines below
# player1 = PlayerCharacter(3,3)
# player2 = PlayerCharacter.adding_things(1,1)
player1 = PlayerCharacter('Tom', 22)

print(f'Using instantiate: {player1.name, player1.age}')
print(f'Using @classmethod to sum the numbers: {PlayerCharacter.adding_things(10, 10)}')
print(f'Using @staticmethod to sum the numbers: {PlayerCharacter.adding_things2(10, 50)}')

# https://www.makeuseof.com/tag/python-instance-static-class-methods/
# Instance Methods: The most common method type. Able to access data and properties unique to each instance.
# Static Methods: Cannot access anything else in the class. Totally self-contained code.
# Class Methods: Can access limited methods in the class. Can modify class specific details.
