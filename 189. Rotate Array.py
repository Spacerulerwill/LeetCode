# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # reverse whole list
        nums.reverse()
        low = 0
        high = k-1
        # reverse from 0 to k-1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        #reverse remaining section of list
        low = k
        high = len(nums)-1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    print(nums)