from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        i = 0
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            candidate = shortest[i]
            if any(str[i] != candidate for str in strs):
                break
        else:
            i = len(shortest)
        return shortest[:i]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["a"]))