class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split("/")
        print(split)

if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/home/"))