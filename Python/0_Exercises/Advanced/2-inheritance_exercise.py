class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


print('1 Add another Cat\n')


class Blue(Cat):
    def sing(self, sounds):
        return f'{sounds}'


print('2 Create a list of all of the pets (create 3 cat instances from the above)\n')

my_cats = [Simon('Simon', 4), Sally('Sally', 10), Blue('Blue', 1)]

print('3 Instantiate the Pet class with all your cats use variable my_pets\n')

my_pets = Pets(my_cats)

print('4 Output all of the cats walking using the my_pets instance\n')

my_pets.walk()
