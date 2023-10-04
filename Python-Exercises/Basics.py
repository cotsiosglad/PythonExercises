a = (1, 2, 3, 4, 5, 6, 7)

#
enumA = (enumerate(a))

print(list(enumA))

print(len(a))

print(range(len(a)))

for i in range(len(a)):
    print(f"Index of range: {i}")
    print(f"Value of a : {a[i]}")
