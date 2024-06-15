# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            if dp[i+2] > dp[i+1]:
                dp[i] = cost[i] + dp[i+1]
            else:
                dp[i] = cost[i] + dp[i+2]
        return min(dp[0], dp[1])

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))