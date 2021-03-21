# Inheritance

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):  # Wizard() is a subclass of User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):  # Archer() is a subclass of User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows of {self.num_arrows}')


wizard1 = Wizard('Merlin', 70)  # instantiate wizard
archer1 = Archer('Robin', 170)  # instantiate archer

# print(isinstance(wizard1, User))  # is instance of User?
# print(wizard1.sign_in())  # is Logged in ?

wizard1.attack()  # wizard is attacking
archer1.attack()  # archer is attacking
