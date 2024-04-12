# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_cur = nums[0]
        max_global = nums[0]
        for num in nums[1:]:
            max_cur = max(num, max_cur + num)
            if max_cur > max_global:
                max_global = max_cur
        return max_global

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(solution.maxSubArray([5,4,-1,7,8]))
