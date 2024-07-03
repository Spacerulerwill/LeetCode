# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        n = len(nums)
        return min(
            nums[n-4] - nums[0], # removed 3 largest
            nums[n-1] - nums[3], # removed 3 smallest
            nums[n-3] - nums[1], # removed 2 largest 1 smallest
            nums[n-2] - nums[2]  # removed 1 largest 2 smallest
        )

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDifference([5,3,2,4]))
    print(solution.minDifference([1,5,0,10,14]))
    print(solution.minDifference([3,100,20]))