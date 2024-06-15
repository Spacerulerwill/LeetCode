# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min1 = float("inf")
        min2 = float("inf")

        for num in nums:
            if num < min1:
                min1 = num
            if num > min1:
                min2 = min(num, min2)
            if num > min2:
                return True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet([1,2,3,4,5]))