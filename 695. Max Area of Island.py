# #https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        _max = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                area = 1
                queue = []
                grid[r][c] = 0
                queue.append((r,c))
                while len(queue) != 0:
                    current_r,current_c= queue.pop(0)
                    for dr, dc in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_r = current_r + dr
                        new_c = current_c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            # Check if the new cell is accessible (value is 1)
                            if grid[new_r][new_c] == 1:
                                queue.append((new_r, new_c))
                                grid[new_r][new_c] = 0
                                area += 1
                _max = max(_max, area)
        return _max


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]))