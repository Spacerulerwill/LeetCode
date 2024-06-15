# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        factors = [1]
        i = 2
        while i*i < num:
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
            i += 1
        return sum(factors) == num
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPerfectNumber(28))
    print(solution.checkPerfectNumber(7))