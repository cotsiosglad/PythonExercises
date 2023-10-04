def solution(A):
    # e.g. given an array A[1, 2, 1, 2, 3]. The value 2 should be output as it's the only value that isn't paired

    A.sort()  # Sort list to [1 1 2 2 3]
    for i in range(len(A)):  # for i in range(Length of A is : 5) so 0-4
        print(f"For loop Iteration: {i}")
        print(f"Comparing between {A[i]} and {A[i + 1]}")
        if A[i] != A[i + 1]:
            print(A[i])
        else:
            print("Pairs found\n")
        if len(A) < i + 1:
            break


solution([1, 2, 1, 2, 3])
