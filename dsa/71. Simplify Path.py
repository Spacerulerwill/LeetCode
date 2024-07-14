# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [directory for directory in path.split("/") if len(directory) > 0]
        print(directories)
        stack = []
        for directory in directories:
            if directory == ".":
                 continue
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)
        return "/" + "/".join(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/home/"))
    print(solution.simplifyPath("/home//foo/"))    
    print(solution.simplifyPath("/home/user/Documents/../Pictures"))    
    print(solution.simplifyPath("/.../a/../b/c/../d/./"))    
    print(solution.simplifyPath("/../"))