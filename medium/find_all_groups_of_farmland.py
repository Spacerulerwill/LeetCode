# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        farmland = []
        rows = len(land)
        cols = len(land[0])

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    land[r][c] = 0
                    
                    # start position
                    start_r = r
                    start_c = c

                    # end position
                    end_r = r
                    end_c = c

                    # extend sideways
                    while end_c < cols - 1 and land[end_r][end_c + 1] == 1:
                        end_c += 1
                        # zero out
                        land[end_r][end_c] = 0

                    # extend downwards
                    while end_r < rows - 1 and land[end_r + 1][end_c] == 1:
                        end_r += 1
                        # zero out
                        for i in range(start_c, end_c+1):
                            land[end_r][i] = 0
                    farmland.append([start_r, start_c, end_r, end_c])
        return farmland
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findFarmland([[0,1], [1,0]]))
    print(solution.findFarmland([[1,0,0],[0,1,1],[0,1,1]]))
    print(solution.findFarmland([[1,1],[1,1]]))
    print(solution.findFarmland([[0]]))