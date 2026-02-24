import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set(string.ascii_letters + string.digits)
        s = "".join(char for char in s if char in alphanumeric).lower()
        return s == s[::-1]