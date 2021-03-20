# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply():
    list_numbers = [8, 2, 3, -1, 7]

    numbers = 1

    for i in list_numbers:
        numbers *= i
    print(numbers)


multiply()
