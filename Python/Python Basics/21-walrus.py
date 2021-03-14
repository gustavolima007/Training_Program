# Walrus - Add := in the code

a = 'Hollywood'

# if (len(a) > 10):
#    print(f'Too long {len(a)} elements')

if (n := len(a)) > 10:
    print(f'Too long {n} elements')

# Now n = len(a), using :=
print('\n')

# Other example using While loop
while (n := len(a)) > 1:
    print(n)

    a = a[:-1]

print(a)
