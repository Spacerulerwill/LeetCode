# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("  hello world  "))