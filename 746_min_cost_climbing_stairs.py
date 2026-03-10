from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0 for _ in range(len(cost))]
        memo[-1] = cost[-1]
        memo[-2] = cost[-2]
        for i in range(-3, -len(cost) - 1, -1):
            memo[i] = cost[i] + min(memo[i + 1], memo[i + 2])
        return min(memo[0], memo[1])


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
