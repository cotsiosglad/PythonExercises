# PermMissingElem: Given an array A of N integers, where each integer is unique and ranges from 1 to N+1, the goal is
# to find the missing integer in the array.

def solution(A):
    # Calculate the expected sum of integers in the range 1 to N+1
    N = len(A)
    expected_sum = (N + 2) * (N + 1) // 2

    # Calculate the actual sum of integers in the array
    actual_sum = sum(A)

    # The missing integer is the difference between the expected sum and the actual sum
    missing_int = expected_sum - actual_sum

    return missing_int


# Take user input for the array A
A = input("Enter the array of integers (separated by commas): ")

# Validate input: make sure A is not empty
if len(A) == 0:
    print("Error: input array is empty.")
    exit()

# Convert input string to a list of integers
A = [int(x) for x in A.split(",")]

# Validate input: make sure each integer is between 1 and len(A)+1
for x in A:
    if x < 1 or x > len(A) + 1:
        print("Error: input integers must be between 1 and len(A)+1.")
        exit()

# Call the solution function and print the result
missing_int = solution(A)
print("The missing integer is:", missing_int)
