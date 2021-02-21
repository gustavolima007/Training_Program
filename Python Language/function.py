def simple():
    print ("My first Function \n")

simple()


# This function can sum the number with 10
def plus_ten(a):
    return a + 10

print("My second function: \n",plus_ten(2))
print(plus_ten(5), "\n")


# This function will calculate the wage (25 dollars per hour) and the bonus (50 dollars per hour)
def wage(w_hours):
    return w_hours * 25
def with_bonus(w_hours):
    return wage(w_hours) + 50

# Hours 8 per day, just 4 hour with bonus
print("Wage of time worked: $", wage(8), "Dollars", "\nBonus received of a good work: $", with_bonus(4), "Dollars")
