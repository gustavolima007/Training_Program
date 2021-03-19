# Using a for loop and .append() method append each item with a Dr. prefix to the lst.

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]

for i in lst1:
    lst2.append(f"Dr. {i}")

print(lst2)
