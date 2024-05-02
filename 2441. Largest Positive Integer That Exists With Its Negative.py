# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        _max = -1
        for num in nums:
            if -num in seen:
                _max = max(_max, abs(num))
            else:
                seen.add(num)
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxK([-1,2,-3,3]))
