Participants = ["John", "Leila", "Gregory", "Cate", "Pamonha", "Mostro de academia"]
print (Participants)

#Slicing; Just 1 and 3
print (Participants[1:3])

#The first 3
print (Participants[:3])

#After 2 Participants
print (Participants[2:])

#Inverting
print (Participants[-2:])

#Discovering where is Pamonha in the list
print(Participants.index("Pamonha"))

#Taking two list together
Newcomers = ["Joshua", "Brittany"]
print (Newcomers)

Bigger_List = [Participants, Newcomers]
print (Bigger_List)

#changing order of the list
Participants.sort(reverse=True)
print (Participants)

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Numbers.sort()
print (Numbers)

#Tuples (Atribuição de tuplas)
x = (40, 41, 42)
print (x)

y = 40, 50, 30
print (y)

a, b, c = 1, 4, 6
print(b)

print(x[2])

#Tuples together
List = [x, y]
print(List)

(age, years_of_school) = "30,17".split(",")
print(age)
print(years_of_school)

def square_info(x):
    A = x ** 2
    P = 4 * x
    print ("Area and Perimeter: ")
    return A, P
print (square_info(3))
