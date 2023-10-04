# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        uniqueNum = 0
        for num in nums:
            uniqueNum ^= num
        return uniqueNum
    
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.singleNumber([2,2,1,2,2]),
        solution.singleNumber([2,2,3,3,4,4,5])
    )