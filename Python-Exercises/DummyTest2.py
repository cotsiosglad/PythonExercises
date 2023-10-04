def minpositive(A):
    """Given an list A of N integers,
    returns the smallest positive integer (greater than 0)
    that does not occur in A in O(n) time complexity

        Args:
            A: list of integers
        Returns:
            integer: smallest positive integer

        e.g:
            A = [1,2,3]
            smallest_positive_int = 4
    """
    len_nrs_list = len(A)
    N = set(range(1, len_nrs_list + 2))
    print(len(A))
    print(N)
    print(set(A))
    return min(N - set(A))  # gets the min value using the N integers


print(minpositive([1, 5, 8]))
print("*******")
print(minpositive([-1, -3]))
