# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        first_gap = (numRows - 1) * 2
        second_gap = 0
        for i in range(numRows):
            row = ""
            idx = i
            while True:
                if first_gap != 0:
                    if idx < len(s):
                        row += s[idx]
                        idx += first_gap
                    else:
                        break
                if second_gap != 0:
                    if idx < len(s):
                        row += s[idx]
                        idx += second_gap  
                    else:
                        break     
            first_gap -= 2
            second_gap += 2
            result += row
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 1))
    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("PAYPALISHIRING", 4))