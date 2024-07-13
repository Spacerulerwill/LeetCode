# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # bottom row
        i = cols-1
        while i >= 0 and obstacleGrid[rows-1][i] == 0:
            dp[rows-1][i] = 1
            i -= 1
        # right column
        i = rows-1
        while i >= 0 and obstacleGrid[i][cols-1] == 0:
            dp[i][cols-1] = 1
            i -= 1
        # dp
        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
        return dp[0][0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))