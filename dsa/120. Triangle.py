# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTotal([[2],[3,4],[6,5,4],[4,1,8,3]]))
    print(solution.minimumTotal([[-1],[2,3],[1,-1,-3]]))
    print(solution.minimumTotal([[2],[3,4],[6,5,9],[4,4,8,0]]))