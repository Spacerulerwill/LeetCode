# https://leetcode.com/problems/valid-triangle-number/
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.triangleNumber([2,2,3,4]))