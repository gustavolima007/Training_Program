# 4. Write a Python program to reverse a string.
# Sample String : c
# Expected Output : "dcba4321"

def reverse_func():
    '''This function will reverse the phrase bellow "123abcd"'''
    phrase = "1234abcd"[::-1]

    print(phrase)


def reverse_input(x):
    '''This function will show a input that will reverse everything'''
    return x[::-1]

print(reverse_func.__doc__)
reverse_func()

print(reverse_input.__doc__)
print(reverse_input(input('Put something to reverse: ')))
