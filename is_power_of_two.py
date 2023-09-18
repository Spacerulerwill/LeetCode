# https://leetcode.com/problems

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0
    
if __name__ == "__main__":
    solution = Solution()

    for i in range(1, 257):
        print(f"{i}: {solution.isPowerOfTwo(i)}")