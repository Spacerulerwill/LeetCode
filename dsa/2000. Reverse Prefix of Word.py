# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        low = 0
        try:
            high = word.index(ch)
        except ValueError:
            return word     
        word_split = list(word)
        while low < high:
            word_split[low], word_split[high] = word_split[high], word_split[low]
            low += 1
            high -= 1
        return "".join(word_split)

if __name__ == "__main__":
    solution = Solution()