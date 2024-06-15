# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1
        return len(t) - j

if __name__ == "__main__":
    solution = Solution()
    print(solution.appendCharacters("lbg", "g"))
    print(solution.appendCharacters("a", "z"))