# https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        # create set of queen positions so we can check if a position if a queen in O(1)
        queen_set = set(tuple(coord) for coord in queens)
        output_queens = []
        for direction in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]:
            start = king[:]
            while start[0] >= 0 and start[0] < 8 and start[1] >= 0 and start[1] < 8 and (king[0], king[1]):
                if tuple(start) in queen_set:
                    output_queens.append(start)
                    break
                start[0] += direction[0]
                start[1] += direction[1]
        return output_queens

if __name__ == "__main__":
    solution = Solution()
    print(solution.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]))