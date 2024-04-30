# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(open:int=0, closed:int=0, path:str=""):
            if open == closed == n:
                res.append(path)
                return
            if open < n:
                backtrack(open + 1, closed, path + "(")
            if closed < open:
                backtrack(open, closed + 1, path + ")")
        backtrack()
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))