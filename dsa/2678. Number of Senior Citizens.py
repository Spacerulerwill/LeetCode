# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for detail in details if int(detail[11:13]) > 60 )

if __name__ == "__main__":
    solution  = Solution()
    print(solution.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))