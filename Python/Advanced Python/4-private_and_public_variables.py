# Private vs Public Variables
# we use underscore to turn a variable in private
# _name
# _age

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name # this is a private variable - _name
        self._age = age # private - _age

    def run(self):
        print(f'Run {self._name} now!')

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('Gustavo', 22)

print(player1.speak())

print(player1.run())