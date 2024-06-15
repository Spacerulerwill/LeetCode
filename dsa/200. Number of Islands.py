# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # breadth first search island we have found, marking all 1s as visited (z)
                    queue = []
                    islands += 1
                    grid[r][c] = "0"
                    queue.append((r,c))
                    while len(queue) != 0:
                        current_r,current_c= queue.pop(0)
                        for dr, dc in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_r = current_r + dr
                            new_c = current_c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols:
                                # Check if the new cell is accessible (value is 1)
                                if grid[new_r][new_c] == "1":
                                    queue.append((new_r, new_c))
                                    grid[new_r][new_c] = "0"
        return islands

if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))