# https://leetcode.com/problems/unique-paths-iii

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # linear search to find starting square
        empty = 0
        for rowIdx, row in enumerate(grid):
            for colIdx, val in enumerate(row):
                if val == 1:
                    startRow = rowIdx
                    startCol = colIdx
                elif val == 0:
                    empty += 1

        visited = set()
        uniquePaths = 0
        def backtrack(visited: set[tuple[int, int]], r:int, c:int):
            nonlocal uniquePaths
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] == -1:
                return
            if grid[r][c] == 2 and len(visited) - 1 == empty:
                uniquePaths += 1
                return
            visited.add((r,c))
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                backtrack(visited, r+dr, c+dc)
            visited.remove((r,c))
        backtrack(visited, startRow, startCol)
        return uniquePaths
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))