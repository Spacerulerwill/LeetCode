# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        k = n & 0b01010101010101010101010101010101
        j = n & 0b10101010101010101010101010101010
        return k > 0 and k & (k-1) == 0 and j == 0


if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 65):
        print(f"{i}: {solution.isPowerOfFour(i)}")