def solution(A):
    # Add a set of integers in A
    set_A = set(A)

    # Iterate over positive integers starting from 1, in this case ( 1, 3+2 ) so from 1-4. Range ignores last element
    for i in range(1, len(A) + 2):
        # If i is not in set_A, return i as the smallest positive integer not in A
        if i not in set_A:
            return i


A = [-1, -3]
print(solution(A))
