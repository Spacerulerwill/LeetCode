class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeStars("leet**cod*e"))