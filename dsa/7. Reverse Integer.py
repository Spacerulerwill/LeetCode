# https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        reversed = 0
        sign = -1 if x < 0 else 1
        temp = abs(x)

        while temp != 0:
          digit = temp % 10
          reversed = reversed * 10 + digit
          temp //= 10

        return reversed * sign if reversed < 2**31 else 0

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.reverse(123),
        solution.reverse(-456)
    )
