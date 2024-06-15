# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return x
        low = 0
        high = x // 2
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif x > mid_squared:
                low = mid + 1
            else:
                high = mid -1
        return high
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
