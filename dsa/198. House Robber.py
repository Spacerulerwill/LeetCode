# https://leetcode.com/problems/house-robber/

# O(n) time, O(n) space
class Solution1:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

# O(n) time, O(1) space  
class Solution2:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        second_previous = nums[0]
        previous = max(nums[0], nums[1])
        current = 0
        for i in range(2, len(nums)):
            current = max(second_previous + nums[i], previous)
            second_previous = previous
            previous = current
        return current
    
if __name__ == "__main__":
    solution = Solution2()
    print(solution.rob([2,7,9,3,1]))
    print(solution.rob([2,1,1,2]))