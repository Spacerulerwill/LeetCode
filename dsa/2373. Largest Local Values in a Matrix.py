# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        def largestLocalMatrix(r:int, c:int):
            return max(grid[r+i][c+j] for i in range(3) for j in range(3))
        output = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for r in range(n-2):
            for c in range(n-2):
                output[r][c] = largestLocalMatrix(r,c)
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestLocal([
        [9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]))