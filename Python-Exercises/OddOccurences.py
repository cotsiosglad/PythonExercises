def solution(A):
    # e.g. given an array A[1, 2, 1, 2, 3]. The value 2 should be output as it's the only value that isn't paired

    # Initialize an empty dictionary to store the count of each element in the array
    dict = {}

    # Iterate through each element in the array A: 1, 2, 1, 2, 3, 4
    for i in range(len(A)): # Range is 0,6 so 0,1,2,3,4,5
        # Assign the current element to the variable num
        num = A[i]
        print(f"Value being stored in num from array: {num}")
        # Check if the current element already exists in the dictionary
        if num not in dict:
            # If not, add it to the dictionary with a count of 1
            dict[num] = 1
        else:
            # If it already exists, increment the count for that element by 1
            dict[num] = dict[num] + 1

    # Print the dictionary for debugging purposes
    print(dict)

    # Find the key in the dictionary with the minimum value (i.e. the unpaired element)
    # The key parameter for the min function specifies that the minimum value should be determined
    # by the value returned by the get method for each key in the dictionary
    unpaired_element = min(dict, key=dict.get)

    # Print the unpaired element to the console
    print(unpaired_element)


solution([1, 2, 1, 2, 3, 4])
