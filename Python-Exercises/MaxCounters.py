# Given an integer N and an array A of M integers, where each integer is in the range [1, N+1], the goal is to
# perform a series of operations on a counter array of size N. Each operation is either an increment operation or a
# max counter operation.

def max_counters(N, A):
    counters = [0] * N
    max_counter = 0
    last_max_counter = 0
    for i in range(len(A)):
        if A[i] == N + 1:
            last_max_counter = max_counter
        else:
            if counters[A[i] - 1] < last_max_counter:
                counters[A[i] - 1] = last_max_counter
            counters[A[i] - 1] += 1
            if counters[A[i] - 1] > max_counter:
                max_counter = counters[A[i] - 1]
    for i in range(len(counters)):
        if counters[i] < last_max_counter:
            counters[i] = last_max_counter
    return counters


# Take user input
N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))
A = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Call the function and print the result
result = max_counters(N, A)
print(result)
