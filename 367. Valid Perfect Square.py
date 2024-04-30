class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 0
        high = num // 2
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            if mid_squared == num:
                return True
            elif num > mid_squared:
                low = mid + 1
            else:
                high = mid - 1
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPerfectSquare(1))
    print(solution.isPerfectSquare(2))
    print(solution.isPerfectSquare(4))
    print(solution.isPerfectSquare(16))