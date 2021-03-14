# *args / **kwargs

# how to use args and kwargs


# write a function - Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('James Bond', 2, 2, 2, 2, num1=2, num2=2))


# another example
def my_func(**kwargs):
    print(kwargs.values())
    return(kwargs)


my_func(result=50, result2=50)
