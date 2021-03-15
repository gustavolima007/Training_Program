# exercise
import datetime
birth_year = input('What year were you born?')

x = datetime.datetime.now()
current_year = x.year
user_age = current_year - int(birth_year)

print(f'Your age is: {user_age}')
