# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        result = 0
        for i in range(len(points)):
            point1 = points[i]
            gradients = {}
            for j in range(i+1, len(points)):
                point2 = points[j]
                change_in_y = point2[1] - point1[1]
                change_in_x = point2[0] - point1[0]
                gradient = float("inf") if change_in_x == 0 else (change_in_y / change_in_x) 
                if gradient not in gradients:
                    gradients[gradient] = 1
                else:
                    gradients[gradient] += 1
            if len(gradients) > 0:
                result = max(max(gradients.values()), result)
        return result+1

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPoints([[1,1],[2,2],[3,3]]))
    print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(solution.maxPoints([[0,0]]))