# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        bracket_dict = {
            ")": "(",
            "}" : "{",
            "]": "["
        }
        
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if len(stack) == 0 or stack.pop() != bracket_dict[char]:
                    return False
        return len(stack) == 0
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(""))
    print(solution.isValid("({})"))
    print(solution.isValid("(({))"))