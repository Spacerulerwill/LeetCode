# https://leetcode.com/problems/basic-calculator-ii
class Solution:
    def calculate(self, s: str) -> int:
        last_operand = 1
        last_operator = "*"
        current_operator = None
        total = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
                continue
            if char.isdigit():
                # consume operand
                operand = 0
                while i < len(s) and s[i].isdigit():
                    operand = operand * 10 + int(s[i])
                    i += 1
                i -= 1
                if current_operator:
                    match current_operator:
                        case "+":
                            total += operand
                            last_operator = "+"
                            last_operand = operand
                            last_operand = operand
                        case "-":
                            total -= operand
                            last_operator = "-"
                            last_operand = operand
                            last_operand = operand
                        case "*":
                            if last_operator == "+":
                                total -= last_operand
                                total += (last_operand * operand)
                                last_operator = "+"
                                last_operand = last_operand * operand
                            elif last_operator == "-":
                                total += last_operand
                                total -= (last_operand * operand)
                                last_operator = "-"
                                last_operand = (last_operand * operand)
                            else:
                                total *= operand
                                last_operator = "*"
                        case "/":
                            if last_operator == "+":
                                total -= last_operand
                                total += (last_operand // operand)
                                last_operator = "+"
                                last_operand = last_operand // operand
                            elif last_operator == "-":
                                total += last_operand
                                total -= (last_operand // operand)
                                last_operator = "-"
                                last_operand = (last_operand // operand)
                            else:
                                total //= operand
                                last_operator = "/"
                else:
                    total = operand
            else:
                current_operator = char
            i += 1
        return total
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("1+2*5/3+6/4*2"))