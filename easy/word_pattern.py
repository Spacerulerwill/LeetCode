class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        word_map = {}
        words_used = set()
        for char, word in zip(pattern, words):
            if char in word_map:
                if word_map[char] != word:
                    return False
            elif word in words_used:
                return False
            else:
                word_map[char] = word
                words_used.add(word)
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("aaaa", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))
