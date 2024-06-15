# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_vowels = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        _max = current_vowels
        left = 0
        right = k - 1
        for i in range(len(s) - k):
            if s[right+1] in vowels:
                current_vowels += 1
            if s[left] in vowels:
                current_vowels -= 1
            left += 1
            right += 1
            _max = max(_max, current_vowels)
        return _max
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels("abciiidef", 3))