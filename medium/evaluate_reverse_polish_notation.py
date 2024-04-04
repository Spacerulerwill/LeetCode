# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens: 
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                match token:
                    case "+":
                        stack.append(first_num + second_num)
                    case "*":
                        stack.append(first_num * second_num)
                    case "-":
                        stack.append(first_num - second_num)
                    case "/":
                        stack.append(int(first_num / second_num))
        return stack[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))