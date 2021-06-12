# write a code with a question, "From 1 to 10, try to guess the number to win!"
# if he guess a number, and got it right, show a win messenger, else, try again!
# use While loop


response = int(input('From 1 to 10, try to guess the number: '))

while response == 7:
    print("Perfect shoot!")
    break
else:
    print('Wrong number, try again!')
