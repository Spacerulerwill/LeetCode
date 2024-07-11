# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        # create a copy with all parenthesis removed
        new = [char for char in s if char not in {"(", ")"}]   
        parenthesis_seen = 0  
        for idx, char in enumerate(s):
            # our index in the string without the opening parenthesis
            # add index in new to stack if its open
            if char == "(":
                stack.append(idx - parenthesis_seen)
                parenthesis_seen += 1
            # if its closed, pop open index calculate close bracket index and reverse
            elif char == ")":
                parenthesis_seen += 1
                idx_in_new = idx - parenthesis_seen
                start_idx = stack.pop()
                while start_idx < idx_in_new:
                    new[start_idx], new[idx_in_new] = new[idx_in_new], new[start_idx]
                    start_idx += 1
                    idx_in_new -= 1
        return "".join(new)
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseParentheses("(u(love)i)"))