# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # bottom row
        sum = 0
        for col in range(cols-1, -1, -1):
            sum += grid[rows-1][col]
            dp[rows-1][col] = sum
        # right column
        sum = 0
        for row in range(rows-1, -1, -1):
            sum += grid[row][cols-1]
            dp[row][cols-1] = sum
        # do the dp
        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
        for row in dp:
            print(row)
        # return final
        return dp[0][0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))