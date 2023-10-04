# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


class Solution:
    def isPalindrome(self, x):
        x = str(x)
        for i in range(0, len(x)):
            print("Index: " + str(i))
            print("Value: " + str(x[i]))


sol = Solution()

sol.isPalindrome(120)
