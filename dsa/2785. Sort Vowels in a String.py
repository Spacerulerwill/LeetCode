# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_map = {
            "A": 0,
            "E": 0,
            "I": 0,
            "O": 0,
            "U": 0,
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
        }
        total_vowels = 0
        for char in s:
            if char in vowel_map:
                vowel_map[char] += 1
                total_vowels += 1
        sorted = ["" for _ in range(total_vowels)]
        i = 0
        for vowel, count in vowel_map.items():
            for _ in range(count):
                sorted[i] = vowel
                i += 1
        i = 0
        s = list(s)
        for j in range(len(s)):
            if s[j] in vowel_map:
                s[j] = sorted[i]
                i += 1
        return "".join(s)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortVowels("lEetcOde"))