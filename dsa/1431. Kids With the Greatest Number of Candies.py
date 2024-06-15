# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        return [ith_candies + extraCandies >= maxCandies for ith_candies in candies]

if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([2,3,5,1,3], 3))