# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

list = [1, 2, 3, 3, 3, 3, 4, 4, 5]


def unique():
    filter_list = []

    for i in list:
        if i not in filter_list:
            filter_list.append(i)

    print(filter_list)


unique()
