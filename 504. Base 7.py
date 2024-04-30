# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        result = ""
        negative = num < 0
        num = abs(num)
        while num > 0:
            remainder = num % 7
            num //= 7
            result = str(remainder) + result
        if negative:
            return "-" + result
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToBase7(10))
    print(solution.convertToBase7(-7))