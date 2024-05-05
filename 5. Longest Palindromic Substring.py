# https://leetcode.com/problems/longest-palindromic-substring/

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# A linear solution exists that will never derive by myself
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # palindrome helper function
        def palindrome(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return l + 1, r - 1   
        longest = (0, 0)
        for i in range(len(s)):
            odd = palindrome(i, i)
            if odd[1] - odd[0] > longest[1] - longest[0]:
                longest = odd
            even = palindrome(i, i + 1)
            if even[1] - even[0] > longest[1] - longest[0]:
                longest = even
        return s[longest[0]: longest[1] + 1] 

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("cbbd"))