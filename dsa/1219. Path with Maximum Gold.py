# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        def backtrack(r: int, c: int, total_gold: int):
            nonlocal _max
            current_gold = grid[r][c]
            grid[r][c] = 0
            _max = max(_max, total_gold)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != 0:
                    backtrack(new_r, new_c, total_gold + grid[new_r][new_c])
            grid[r][c] = current_gold
        _max = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                backtrack(r, c, grid[r][c])
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))