# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        j = 0
        _min = float("inf")
        sum = 0
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                _min = min(_min, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        return 0 if _min == float("inf") else _min
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))