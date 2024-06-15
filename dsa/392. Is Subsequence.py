# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        j = 0
        for ch in t:
            if ch == s[j]:
                j += 1
            if j == len(s):
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence("abc", "ahbgdc"))