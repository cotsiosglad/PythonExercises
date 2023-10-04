def solution(A):
    dict = {}
    for key, val in (enumerate(A)):
        print(f"The Index of array is: {key},and the Value is: {val}")
        num = val
        #print(num)
        if num not in dict:
            dict[num] = 1
            #print(dict)
        else: dict[num] = dict[num] + 1
    print(dict)






solution([5,6,7,8,7,8])