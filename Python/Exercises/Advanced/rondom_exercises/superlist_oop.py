# create a Class that will add numbers

class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(50)
print(super_list1[0])

print(issubclass(SuperList, list))