# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution:
    def validStrings(self, n: int) -> list[str]:
        result = []
        def backtrack(current:list[int], last_was_zero:bool):
            if len(current) == n:
                result.append("".join(str(digit) for digit in current))
                return
            backtrack(current + [1], False)
            if not last_was_zero:
                backtrack(current + [0], True)
        backtrack([], False)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.validStrings(3))