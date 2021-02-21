#While Loops and Incrementing
print("\nWhile Loops and Incrementing: " )
x = 0
while x <= 20:
    print ("Using While Loops", x)
    x += 2

#Create Lists with the range() Function
#RANGE - range(start, stop, step(The distance between the values))
print("\nCreate Lists with the range() Function: " )
x = range(5, 50, 4)
for r in x:
    print(r, end = " ")


#List
print("\n\nList: " )
def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total

list_1 = [1, 3, 4, 5, 15 ,23, 60, 100]

count(numbers)




#arrrumaaarrrr
