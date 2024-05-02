# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        negatives = set(num for num in nums if num < 0)
        _max = -1
        for num in nums:
            if num > 0 and -num in negatives:
                _max = max(_max, num)
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxK([-1,2,-3,3]))