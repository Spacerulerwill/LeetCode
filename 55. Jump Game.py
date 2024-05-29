# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        target_idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            dp[i] = i + nums[i] >= target_idx or any(dp[i + j + 1] for j in range(nums[i]))
        return dp[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2,5,0,0]))