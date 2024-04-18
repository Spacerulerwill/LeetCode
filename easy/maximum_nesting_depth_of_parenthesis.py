# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for char in s:
            match char:
                case "(":
                    depth += 1
                    max_depth = max(max_depth, depth)
                case ")":
                    depth -= 1
        return max_depth

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(solution.maxDepth("(1)+((2))+(((3)))"))