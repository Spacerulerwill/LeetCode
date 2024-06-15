# https://leetcode.com/problems/basic-calculator-ii
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def calculate(self, s: str) -> int:
        current_operand = 0
        total = 0
        last_operator = "+"
        last_operand = 0
        for i, char in enumerate(s):
            if char.isdigit():
                current_operand = current_operand * 10 + int(char)
            if char in {"+", "*", "-", "/"} or i == len(s) - 1:
                if last_operator == "+":
                    total += last_operand
                    last_operand = current_operand
                elif last_operator == "-":
                    total += last_operand
                    last_operand = -current_operand
                elif last_operator == "*":
                    last_operand *= current_operand
                elif last_operator == "/":
                    if last_operand >= 0:
                        last_operand //= current_operand
                    else:
                        last_operand = -((last_operand * -1) // current_operand)
                last_operator = char
                current_operand = 0
        return total + last_operand
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("1+2*5/3+6/4*2"))