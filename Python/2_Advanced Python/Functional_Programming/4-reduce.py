# map, filter, zip, and reduce
# REDUCE

from functools import reduce

my_list = [1, 2, 3, 4, 5]


def accumulator(acc, item):
    print(acc, item)
    # print(5,5)
    return acc + item


print(reduce(accumulator, my_list))
