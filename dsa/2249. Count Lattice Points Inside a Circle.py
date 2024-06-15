# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        unique_points = set()
        for circle in circles:
            center_x = circle[0]
            center_y = circle[1]
            radius = circle[2]
            for x in range(center_x - radius, center_x + radius + 1):
                for y in range(center_y - radius, center_y + radius + 1):
                    if (x - center_x) * (x - center_x) + (y - center_y) * (y - center_y) <= radius * radius:
                        unique_points.add((x,y))
        return len(unique_points)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countLatticePoints([[2,2,1]]))
    print(solution.countLatticePoints([[2,2,2],[3,4,1]]))