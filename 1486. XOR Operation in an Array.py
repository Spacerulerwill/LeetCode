# https://leetcode.com/problems/xor-operation-in-an-array/

from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda a, b: a ^ b, [start+2*i for i in range(n)])
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.xorOperation(5, 0))