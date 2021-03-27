# Scope - What variables do I have access to ?

a = 1


def parent():
    a = 1

    def confusion():
        return sum
    return confusion()


print(parent())
print(a)

# 1 - start with local
# 2 - parent local?
# 3 - Global
# 4 - built in python functions

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
count()
print(count())

# other whey without Global

total2 = 0


def count2(total2):
    # global total2
    total2 += 1
    return total2


# count2(total2)
# count2(total2)
# count2(total2)
print(count2(count2(count2(count2(total2)))))
