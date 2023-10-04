# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n&1
            n = n >> 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.hammingWeight(222),
        solution.hammingWeight(1),
        solution.hammingWeight(23123123)
    )
    