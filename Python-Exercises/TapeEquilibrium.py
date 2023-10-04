# Given an array A of N integers, the goal is to find the minimum absolute difference between the sum of the first
# part of the array and the sum of the second part of the array.


A = input("Enter the array of integers (separated by commas): ")
# Convert input string to a list of integers
A = [int(x) for x in A.split(",")]

if len(A) == 0:
    print("Error: input array is empty.")
    exit()


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


B, C = split_list(A)
firstHalf = sum(B)
secondHalf = sum(C)
print(firstHalf)
print(secondHalf)

diff = int(firstHalf) - int(secondHalf)
print("Difference between first and second half is : " + str(diff))
