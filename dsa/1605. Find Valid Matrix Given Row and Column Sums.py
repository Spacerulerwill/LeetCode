# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                min = min(rowSum[i], colSum[j])
                result[i][j] = min
                rowSum[i] -= min
                colSum[j] -= min
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreMatrix([5,7,10], [8,6,8]))