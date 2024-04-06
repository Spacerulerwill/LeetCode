# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_idx = 0
        end_idx = len(needle) - 1
        while end_idx < len(haystack):
            if needle == haystack[start_idx:end_idx+1]:
                return start_idx
            start_idx += 1
            end_idx += 1
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("leetcode", "leeto"))
    print(solution.strStr("sadbutsad", "sad"))