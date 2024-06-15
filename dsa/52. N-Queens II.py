# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        # check a queen wont be attacked by other queens when it is placed
        def is_queen_valid(r:int, c:int, current_queens:set[tuple[int,int]]) -> bool:
            for q_r, q_c in current_queens:
                if q_r == r or q_c == c or abs(c-q_c) == abs(r-q_r):
                    return False
            return True      
        # backtracking solve function
        def solve(r:int, queens:set[tuple[int,int]]) -> None:
            nonlocal solutions
            if r == n:
                solutions += 1
                return
            for col in range(n):
                if is_queen_valid(r, col, queens):
                    queens.add((r, col))
                    solve(r + 1, queens)
                    queens.remove((r, col))
        solutions = 0
        solve(0,set())
        return solutions

if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))