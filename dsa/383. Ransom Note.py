# https://leetcode.com/problems/ransom-note/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for char, count in ransomCounter.items():
            if magazineCounter.get(char, 0) < count:
                return False
        return True
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("aa", "aab"))