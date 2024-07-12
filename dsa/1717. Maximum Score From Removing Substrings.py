# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        def helper(input, suffix: list[str], score_add:int) -> list[str]:
            nonlocal score
            stack = []
            for char in input:
                stack.append(char)
                while len(stack) >= 2 and stack[-2:] == suffix:
                    stack.pop()
                    stack.pop()
                    score += score_add
            return stack
        
        if y >= x:
            stack = helper(s, ["b", "a"], y)
            helper(stack, ["a", "b"], x)
        else:
            stack = helper(s, ["a", "b"], x)
            print("".join(stack))
            helper(stack, ["b", "a"], y)

        return score
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumGain("cdbcbbaaabab", 4, 5))
    print(solution.maximumGain("aabbaaxybbaabb", 5, 4))