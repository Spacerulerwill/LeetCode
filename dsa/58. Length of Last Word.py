# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        res = 0
        # trailing whitespace
        while s[i] == " ":
            i -= 1
        # read up until whitespace
        while s[i] != " ":
            i -= 1
            res += 1
            if i < 0:
                break
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("aaaa"))