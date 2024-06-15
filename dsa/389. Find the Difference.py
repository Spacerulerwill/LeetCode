# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum(ord(char) for char in s)
        sum2 = sum(ord(char) for char in t)
        return chr(sum2 - sum1)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDifference("abcd", "abcde"))