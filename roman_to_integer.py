# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        for i in range(len(s)):
            if i < len(s) -1 and map[s[i]] < map[s[i+1]]:
                ans -= map[s[i]]
            else:
                ans += map[s[i]]
        
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("LVIII"))
