# https://leetcode.com/problems/sum-of-square-numbers/

from math import ceil, sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(ceil(sqrt(c))) 

        while i <= j:
            val = i * i + j * j
            print(val, i, j)
            if val > c:
                j -= 1
            elif val < c:
                i += 1
            else:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeSquareSum(4))