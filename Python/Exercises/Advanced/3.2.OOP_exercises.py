# OOP Exercise 5: Define property that should have the same value for every class instance
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    # Class attribute
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


work_bus = Bus('Mercedes Benz', 180, 25)
work_car = Car('Onix', 220, 45)

print(f'The model of the bus is {work_bus.name} and the color is {work_bus.color} ok?')
print(f'The model of the car is {work_car.name} and the color is {work_car.color} ok?')
