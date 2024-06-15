# https://leetcode.com/problems/add-digits/

"""
O(n)
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while num > 9:
            digit_sum = 0
            num_save = num
            while num_save > 0:
                digit_sum += num_save % 10
                num_save //= 10
            num = digit_sum
        return num
"""
    
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        res = num % 9
        if res == 0:
            return 9
        else:
            return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(123123))