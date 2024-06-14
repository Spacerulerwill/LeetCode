# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        increments = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increments += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return increments

if __name__ == "__main__":
    solution = Solution()
    print(solution.minIncrementForUnique([1,2,2]))
    print(solution.minIncrementForUnique([3,2,1,2,1,7]))