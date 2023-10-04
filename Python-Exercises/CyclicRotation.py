# Given       3,8,9,7,6
# Rotation 1: 6,3,8,9,7

def solution(N, K):
    print(f"Array before rotation:  {N}")
    # numbers = [3, 8, 9, 7, 6]
    for i in range(1,K+1):
        print(f"Rotation # {i}")
        x = N.pop(-1)
        N.insert(0, x)
        print(N)


solution([3, 8, 9, 7, 6], 4)
