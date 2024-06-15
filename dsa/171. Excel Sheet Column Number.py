# https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for idx, char in enumerate(reversed(columnTitle)):
            result += (ord(char) - 64) * (26**idx)
        return result

if __name__ == "__main__":
    solution = Solution()
    print(ord("A"))
    print(solution.titleToNumber("A"))
    print(solution.titleToNumber("AB"))
    print(solution.titleToNumber("ZY"))