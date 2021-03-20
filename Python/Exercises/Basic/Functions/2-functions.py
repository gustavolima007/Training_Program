# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_numbers():
    list = [8, 2, 3, 0, 7]

    sum_list = 0

    for i in list:
        sum_list += i

    print(sum_list)

sum_numbers()