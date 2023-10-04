# Given an array A of N integers, the goal is to find the index of any element that appears more than N/2 times in
# the array, or to return -1 if there is no such element.

def solution(A):
    n = len(A)
    count = {}
    # count the occurrences of each element in the array
    for i in range(n):
        if A[i] in count:
            count[A[i]] += 1
        else:
            count[A[i]] = 1
    # find the elements that appear more than N/2 times in the array
    result = []
    for key in count:
        if count[key] > n // 2:
            result.append(key)
    # find the index of the elements that appear more than N/2 times in the array
    indices = []
    for i in range(n):
        if A[i] in result:
            indices.append(i)
    if len(indices) > 0:
        return indices
    else:
        return -1


# Take user input for the array
arr = input("Enter array elements separated by space: ").split()
#arr = [int(x) for x in arr]

# Find the dominator
dominator_index = solution(arr)

if dominator_index != -1:
    print("The index of the dominator is", dominator_index)
else:
    print("There is no dominator in the array.")
