# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1.0:
            return 1
        if (x == 0.0):
            return 0.0
        if (n == 1):
            return x
        
        if n < 0:
            n = -n
            x = 1/x

        res = 1
        while n > 0:
            if n % 2:
                res *= x   

            x *= x
            n >>= 1
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2, -2))
    print(solution.myPow(2, 10))
    print(solution.myPow(0.01, -25))