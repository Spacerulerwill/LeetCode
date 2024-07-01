# https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2024-07-01

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # cant have 3 consecutive odds if there are less than 3 elements
        if len(arr) < 3:
            return False
        odd_count = sum(1 for i in range(3) if arr[i] % 2 != 0)
        if odd_count == 3:
            return True
        for i in range(3, len(arr)):
            if arr[i - 3] & 1 == 1:
                odd_count -= 1
            if arr[i] & 1 == 1:
                odd_count += 1
            if odd_count == 3:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeConsecutiveOdds([2,6,4,1]))