# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCounter = [0 for x in range(26)]

        for char in s:
            charCounter[ord(char) - 97] += 1

        for char in t:
            charCounter[ord(char) - 97] -= 1
        
        return not any(count != 0 for count in charCounter)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("ginger", "finger"))
    print(solution.isAnagram("bruh", "2"))
    print(solution.isAnagram("anagram", "nagaram"))