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
