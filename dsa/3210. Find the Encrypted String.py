# https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # reverse string
        s = list(s)[::-1]
        # calculate pivot position
        pivot = len(s) - k
        # reverse left side
        i = 0
        j = pivot-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)
        # reverse right side
        i = pivot
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

if __name__ == "__main__":
    solution = Solution()
    print(solution.getEncryptedString("dart", 3))