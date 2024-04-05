# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = []
        incremented = False
        for digit in reversed(digits):
            if not incremented:
                if digit == 9:
                    result.append(0)
                    continue
                else:
                    result.append(digit + 1)
                    incremented = True
            else:
                result.append(digit)

        if not incremented:
            result.append(1)
        result.reverse()
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9,9]))
