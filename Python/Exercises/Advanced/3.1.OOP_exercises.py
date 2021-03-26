print('\nOOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes\n')


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name  # this attribute is for the exercise 3
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers'


modelX = Vehicle('Tesla Model X', 240, 18)  # add name for the exercise 3

print(modelX.max_speed, modelX.mileage)

print('\nOOP Exercise 2: Create a Vehicle class without any variables and methods\n')

# class Vehicle:
#     pass


print('Finish')

print('\nOOP Exercise 3: Create a child class Bus that will inherit all '
      'of the variables and methods of the Vehicle class.\n')


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        '''This function is a requirement of the exercise 4'''
        return super().seating_capacity(capacity=50)


school_bus = Bus('School Volvo', 180, 12)

print(f'Vehicle name: {school_bus.name}\n Speed: {school_bus.max_speed}\n Mileage: {school_bus.mileage}')

print('OOP Exercise 4: Class Inheritance\n')

# Given:
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.
# seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class. You need to use method overriding.

work_school = Bus('Work Bus', 190, 32)

print(work_school.seating_capacity())
