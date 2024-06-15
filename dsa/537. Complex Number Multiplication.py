# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #split both numbers into real and imaginary parts
        num1_split = num1.split("+")
        num1_real = int(num1_split[0])
        num1_imaginary = int(num1_split[1][:-1])

        num2_split = num2.split("+")
        num2_real = int(num2_split[0])
        num2_imaginary = int(num2_split[1][:-1])

        return f"{(num1_real * num2_real) - (num1_imaginary * num2_imaginary)}+{(num1_real * num2_imaginary) + (num1_imaginary * num2_real)}i"

if __name__ == "__main__":
    solution = Solution()
    print(solution.complexNumberMultiply("1+1i", "1+1i"))
    print(solution.complexNumberMultiply("1+-1i", "1+-1i"))