# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        _max = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            elif nums[i - 1] == 1:
                _max = max(_max, current)
                current = 0
        return max(_max, current)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,1,0,0,0,1]))
    print(solution.findMaxConsecutiveOnes([1,1,1,1,0,1]))