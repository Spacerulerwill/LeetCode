# https://leetcode.com/problems/find-the-winner-of-the-circular-game/s

# O(n) time, O(n) space
class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]
        i = 0
        while len(circle) > 1:
            print(circle)
            i = (i + k - 1) % len(circle)
            del circle[i]
        return circle[0]

if __name__ == "__main__":
    solution = Solution1()
    print(solution.findTheWinner(5, 2))