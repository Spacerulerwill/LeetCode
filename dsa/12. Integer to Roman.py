# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        thousands_symbols = ["", "M", "MM", "MMM"]
        hundreds_symbols = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens_symbols = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        units_symbols = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = (num % 100) // 10
        units = num % 10
        return thousands_symbols[thousands] + hundreds_symbols[hundreds] + tens_symbols[tens] + units_symbols[units]

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1994))