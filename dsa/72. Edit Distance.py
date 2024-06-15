# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        # if one has length 0, distance is other length
        if len(word1) == 0:
            return len(word2)
        
        if len(word2) == 0:
            return len(word1)
        
        # initialise dynamic programming table
        cache = [[0 for _ in range(len(word1) + 1)] for _ in range (len(word2) + 1)]

        # initialise first row and column
        for i in range(len(word1) + 1):
            cache[0][i] = i

        for i in range(len(word2) + 1):
            cache[i][0] = i

        for idx_1, char_1 in enumerate(word2):
            for idx_2, char_2 in enumerate(word1):
                # cache positions
                y = idx_1 + 1
                x = idx_2 + 1
                above_left_cell = cache[y - 1][x - 1]
                if char_1 == char_2:
                    cache[y][x] = above_left_cell
                else:
                    above_cell = cache[y - 1][x]
                    left_cell = cache[y][x-1]
                    cache[y][x] = min(above_cell, left_cell, above_left_cell) + 1
        return cache[len(word2)][len(word1)]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance("bruh", "Bruh2"))
