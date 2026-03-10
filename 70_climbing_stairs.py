class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [0 for _ in range(n + 2)]
        memo[-2] = 1
        memo[-3] = 1

        for i in range(-4, -n - 3, -1):
            memo[i] = memo[i + 1] + memo[i + 2]
        return memo[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))
