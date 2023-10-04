# https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        reversed = 0
        temp = x

        while temp != 0:
          digit = temp % 10
          reversed = reversed * 10 + digit
          temp //= 10
          
        return x == reversed

if __name__ == "__main__":
  solution = Solution()
  print(
    solution.isPalindrome(123),
    solution.isPalindrome(323),
    solution.isPalindrome(-555)
  )     
