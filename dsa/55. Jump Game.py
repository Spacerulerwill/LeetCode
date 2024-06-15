# https://leetcode.com/problems/jump-game/

# first attempt
class SlowSolution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        target_idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            dp[i] = i + nums[i] >= target_idx or any(dp[i + j + 1] for j in range(nums[i]))
        return dp[0]

# second attempt - using car idea
class FastSolution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for num in nums:
            if gas < 0:
                return False
            elif num > gas:
                gas = num
            gas -= 1
        return True

if __name__ == "__main__":
    solution = FastSolution()
    print(solution.canJump([2,5,0,0]))