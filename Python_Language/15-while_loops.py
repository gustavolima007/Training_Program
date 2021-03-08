# While Loops

# While Loops for complex situations, and For Loops for simple operations


# infinite loop - don't run this code

# i = 0
# while i < 50:
#   print(i)

# to finish the loop, we use Break
i = 0
while i < 10:
    print(i)
    i += 1 # this line will stop the loop
else:
    print('Done with all the work')

print('\n')

# i = index

# Other example
my_list = [1,2,3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print('\n')

# Question Loop
while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break

print('\n')
