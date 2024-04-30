# https://leetcode.com/problems/excel-sheet-column-title/
from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            remainder = columnNumber % 26
            result = ascii_uppercase[remainder - 1] + result
            columnNumber -= 1
            columnNumber //= 26
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))    
    print(solution.convertToTitle(708))