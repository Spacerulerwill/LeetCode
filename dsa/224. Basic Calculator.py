# https://leetcode.com/problems/basic-calculator/

from enum import Enum

class Token(Enum):
    LEFT_PARENTHESIS = 0
    RIGHT_PARENTHESIS = 1
    ADD = 2
    SUB = 3
    NEGATE = 4

class Solution:
    def calculate(self, s: str) -> int:
        # convert to tokens
        tokens = []
        for char in s:
            match char:
                case "(":
                    tokens.append(Token.LEFT_PARENTHESIS)
                case ")":
                    tokens.append(Token.RIGHT_PARENTHESIS)
                case "+":
                    tokens.append(Token.ADD)
                case "-":
                    if len(tokens) != 0:
                        match tokens[-1]:
                            case Token.ADD | Token.NEGATE | Token.LEFT_PARENTHESIS:
                                tokens.append(Token.NEGATE)
                            case _:
                                tokens.append(Token.SUB)
                    else:
                        tokens.append(Token.NEGATE)
                case char if char.isdigit():
                    if len(tokens) != 0:
                        match tokens[-1]:
                            case int():
                                tokens[-1] = (tokens[-1] * 10) + int(char)
                            case _:
                                tokens.append(int(char))
                    else:
                        tokens.append(int(char))

        # convert tokens to reverse polish notation
        rpn = []
        operator_stack = []
        parenthesis_unary_stacks = []
        token_idx = 0
        while token_idx < len(tokens):
            token = tokens[token_idx]
            match token:
                case int():
                    rpn.append(token)
                case Token.ADD | Token.SUB:
                    if len(operator_stack) == 0 or operator_stack[-1] == Token.LEFT_PARENTHESIS:
                        operator_stack.append(token)
                    else:
                        while len(operator_stack) != 0:
                            if operator_stack[-1] != Token.LEFT_PARENTHESIS:
                                rpn.append(operator_stack.pop())
                            else:
                                break
                        operator_stack.append(token)
                case Token.NEGATE:
                    unary_stack = [token]
                    while tokens[token_idx + 1] == Token.NEGATE:
                        unary_stack.append(Token.NEGATE)
                        token_idx += 1
                    match tokens[token_idx + 1]:
                        case int():
                            rpn.append(tokens[token_idx + 1])
                            rpn.extend(unary_stack)
                            token_idx += 1
                case Token.LEFT_PARENTHESIS:
                    unary_operators = []
                    if token_idx > 0:
                        while tokens[token_idx - 1] == Token.NEGATE:
                            unary_operators.append(Token.NEGATE)
                            token_idx -= 1
                        token_idx += len(unary_operators)
                    parenthesis_unary_stacks.append(unary_operators)
                    operator_stack.append(token)
                case Token.RIGHT_PARENTHESIS:
                    while len(operator_stack) != 0:
                        if operator_stack[-1] != Token.LEFT_PARENTHESIS:
                            rpn.append(operator_stack.pop())
                        else:
                            operator_stack.pop()
                            break
                          
                    if len(parenthesis_unary_stacks) != 0:
                        rpn.extend(parenthesis_unary_stacks.pop())
            token_idx += 1
        while len(operator_stack) != 0:
            rpn.append(operator_stack.pop())

        # evaluate reverse polish notation
        evaluation_stack = []
        for token in rpn:
            match token:
                case int():
                    evaluation_stack.append(token)
                case Token.ADD:
                    operand_2 = evaluation_stack.pop()
                    operand_1 = evaluation_stack.pop()
                    evaluation_stack.append(operand_1 + operand_2)
                case Token.SUB:
                    operand_2 = evaluation_stack.pop()
                    operand_1 = evaluation_stack.pop()
                    evaluation_stack.append(operand_1 -  operand_2)
                case Token.NEGATE:
                    operand = evaluation_stack.pop()
                    evaluation_stack.append(operand * -1)
        return evaluation_stack[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("- (3 + (4 + 5))"))