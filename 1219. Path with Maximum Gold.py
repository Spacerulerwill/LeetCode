# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        def backtrack(r:int, c:int, seen:set[tuple[int,int]], total_gold:int):
            nonlocal _max
            cant_go_up = r == 0 or grid[r-1][c] == 0 or (r-1,c) in seen
            cant_go_down = r == rows-1 or grid[r+1][c] == 0 or (r+1,c) in seen
            cant_go_left = c == 0 or grid[r][c-1] == 0 or (r,c-1) in seen
            cant_go_right = c == cols - 1 or grid[r][c+1] == 0 or (r, c+1) in seen
            if cant_go_up and cant_go_down and cant_go_left and cant_go_right:
                _max = max(_max, total_gold)
                return
            # go up
            if r > 0 and grid[r-1][c] != 0 and (r-1,c) not in seen:
                seen.add((r-1, c))
                backtrack(r-1, c, seen, total_gold + grid[r-1][c])
                seen.remove((r-1, c))
            # go down
            if r < rows-1 and grid[r+1][c] != 0 and (r+1,c) not in seen:
                seen.add((r+1, c))
                backtrack(r+1, c, seen, total_gold + grid[r+1][c])
                seen.remove((r+1, c))
            # go left
            if c > 0 and grid[r][c-1] != 0 and (r,c-1) not in seen:
                seen.add((r, c-1))
                backtrack(r, c-1, seen, total_gold + grid[r][c-1])
                seen.remove((r, c-1))
            # go right
            if c < cols - 1 and grid[r][c+1] != 0 and (r,c+1) not in seen:
                seen.add((r, c+1))
                backtrack(r, c+1, seen, total_gold + grid[r][c+1])
                seen.remove((r, c+1))

        _max = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                backtrack(r, c, {(r,c)}, grid[r][c])
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))