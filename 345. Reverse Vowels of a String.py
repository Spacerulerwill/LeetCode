# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        low = 0
        high = len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s = list(s)
        while low < high:
            while low < high and s[low] not in vowels:
                low += 1
            while low < high and s[high] not in vowels:
                high -= 1
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return "".join(s)

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("hello"))