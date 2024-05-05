# https://leetcode.com/problems/expression-add-operators/

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        def backtrack(expression:str="", total:int=0, idx: int=0, last_operation:str="*", last_operand:int=1):
            if idx == len(num):
                if total == target:
                    res.append(expression)
                return       
            for i in range(idx, len(num)):
                # Skip leading zeros
                if i > idx and num[idx] == '0':
                    break
                
                current_num = num[idx:i+1]
                current_num_int = int(current_num)
                
                if idx == 0:
                    # First number, start the expression
                    backtrack(current_num, current_num_int, i + 1)
                else:
                    # Try all operators
                    backtrack(expression + "+" + current_num, total + current_num_int, i + 1, "+", current_num_int)
                    backtrack(expression + "-" + current_num, total - current_num_int, i + 1, "-", current_num_int)

                    match last_operation:
                        case "+":
                            backtrack(expression + "*" + current_num, (total-last_operand) + (last_operand * current_num_int), i + 1, "+", (last_operand * current_num_int))
                        case "-":
                            backtrack(expression + "*" + current_num, (total+last_operand) - (last_operand * current_num_int), i + 1, "-", (last_operand * current_num_int))
                        case "*":
                            backtrack(expression + "*" + current_num, total * current_num_int, i + 1, "*", current_num_int)
        backtrack()
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.addOperators("123456789", 45))