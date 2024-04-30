class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        low = 0
        high = len(s) - 1
        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                low_alnum = s[low].isalnum()
                high_alnum = s[high].isalnum()

                if low_alnum and high_alnum:
                    return False
                if not low_alnum:
                    low += 1
                if not high_alnum:
                    high -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("race car"))