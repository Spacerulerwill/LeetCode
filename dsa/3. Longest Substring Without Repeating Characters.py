# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        characters = set()
        max_len = 0
        low = 0
        high = 0
        while high < len(s):
            if s[high] in characters:
                while s[high] in characters:
                    characters.remove(s[low])
                    low += 1
            characters.add(s[high])
            max_len = max(max_len, high - low + 1)
            high += 1
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
        