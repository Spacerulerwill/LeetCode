# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # check a queen wont be attacked by other queens when it is placed
        def is_queen_valid(r:int, c:int, current_queens:set[tuple[int,int]]) -> bool:
            for q_r, q_c in current_queens:
                if q_r == r or q_c == c or abs(c-q_c) == abs(r-q_r):
                    return False
            return True      
        # backtracking solve function
        def solve(r:int, queens:set[tuple[int,int]]) -> None:
            if r == n:
                solutions.append(queens.copy())
                return
            for col in range(n):
                if is_queen_valid(r, col, queens):
                    queens.add((r, col))
                    solve(r + 1, queens)
                    queens.remove((r, col))
        # format solution into string output
        def format_solution(queens:set[tuple[int,int]]):
            rows = [["." for _ in range(n)] for _ in range(n)]
            for q_r, q_c in queens:
                rows[q_r][q_c] = "Q"
            return ["".join(row) for row in rows]
        solutions = []
        solve(0,set())
        return [format_solution(solution) for solution in solutions]

if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))