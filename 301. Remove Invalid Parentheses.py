# https://leetcode.com/problems/remove-invalid-parentheses/

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = []
        seen = set()
        min_edits_made = float("inf")
        def backtrack(current:str="",edits_made:int=0,idx:int=0,open:int=0, closed:int=0):
            nonlocal min_edits_made, result, seen
            if idx == len(s):
                if open == closed:
                    if edits_made < min_edits_made:
                        result = [current]
                        seen = {current}
                        min_edits_made = edits_made
                    elif edits_made == min_edits_made:
                        if current not in seen:  # Check if current result is already seen
                            result.append(current)
                            seen.add(current)  # Add current result to seen set
                return
            if s[idx] == "(":
                backtrack(current + "(", edits_made, idx + 1, open + 1, closed)
            elif s[idx] == ")":
                if open > closed:
                    backtrack(current + ")", edits_made, idx + 1, open, closed + 1)
            else:
                backtrack(current + s[idx], edits_made, idx + 1, open, closed)
            backtrack(current, edits_made + 1, idx + 1, open, closed)
        backtrack()
        return result


if __name__ == "__main__":
    solution = Solution()
    # ["(())()","()()()"]
    print(solution.removeInvalidParentheses("()())()"))
