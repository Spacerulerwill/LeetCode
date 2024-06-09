# https://leetcode.com/problems/replace-words/description/

# Trie based solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    # find as much of a word as you can
    def get_word_prefix(self,word):
        curr = self.root
        curr_word = ""
        for c in word:
            if c not in curr.children:
                return word
            curr_word += c
            curr = curr.children[c]
            if curr.end_of_word:
                return curr_word
        return word
    
class TrieSolution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for prefix in dictionary:
            trie.insert(prefix)
        words = sentence.split()
        for i, word in enumerate(words):
            words[i] = trie.get_word_prefix(word)
        return " ".join(words)

if __name__ == "__main__":
    solution = TrieSolution()
    print(solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))