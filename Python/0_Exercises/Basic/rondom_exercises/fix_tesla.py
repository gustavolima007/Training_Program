
#age = input("What is your age?: ")

# if int(age) < 18:
#	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
#	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
#	print("Congratulations on your first year of driving. Enjoy the ride!")

# Wrap the above code in a function called checkDriverAge().
# Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?


def checkDriverAge():

    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
    return age


checkDriverAge()
