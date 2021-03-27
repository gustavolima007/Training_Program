# Magic/Dunder emthods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 88

    def __getitem__(self, item):
        return self.my_dict[item]

    def __call__(self):
        return 'Yes??'


action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))

print(action_figure['name'], action_figure['has_pets'])

print(action_figure())
