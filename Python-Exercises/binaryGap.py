# Write a function: that, given a positive integer N, returns the length of its longest binary gap. The function
# should return 0 if N doesn't contain a binary gap. First we have to convert integer to binary

# Convert Integer to Binary
a = '{0:b}'.format(32)
strA = str(a)
# Split the string using 1 as separator, this will remove all 1s from the string
b = strA.split('1')

# Convert last index value to empty quotes
b[-1] = ''

result = 0
# Enumerate splits the array/tuple in i=index , k = value
for i, k in enumerate(b):
    if len(k) > result:
        result = len(k)

print(a)
print(b)
print(result)
print(b[-1])

10000
