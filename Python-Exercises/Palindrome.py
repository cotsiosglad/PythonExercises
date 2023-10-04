# Palindrome solution using integer division and remainder methods
class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Count the number of digits in x
        num_digits = 0
        temp = x
        while temp > 0:
            num_digits += 1
            temp //= 10

        # Compare the leftmost and rightmost digits, then remove them from x
        for i in range(num_digits // 2):
            leftmost = x // (10 ** (num_digits - 1 - i)) % 10
            rightmost = x % (10 ** (i + 1)) // (10 ** i)
            if leftmost != rightmost:
                return False
        return True

# Palindrome solution using integer to string
# class Solution:
#   def isPalindrome(self, x: int) -> bool:
# Convert integer to string for easier manipulation
#      x = str(x)
# Check if string equals its reverse, if so it's a palindrome
#         return True
#    else:
#       return False
