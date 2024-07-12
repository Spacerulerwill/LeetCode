# https://leetcode.com/problems/unique-paths/

# O(n * m) time, O(n * m) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        # fill in bottom row
        for col in range(n):
            dp[m-1][col] = 1
        # fill in right column
        for row in range(m):
            dp[row][n-1] = 1
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1]
        return dp[0][0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))