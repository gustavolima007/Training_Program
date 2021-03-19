# 3. Write a Python program to get the largest number from a list.

list = [1,2,3,4,5,6,9,9,9,10,20,100,2,3,5]

def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list(list))