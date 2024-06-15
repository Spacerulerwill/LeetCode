# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:                 
        # find farthest left
        low = 0
        high = len(nums)-1
        farthest_left = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                farthest_left = mid
                high = mid - 1  # go left to find earlier occurences
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
     
        # find farthest right
        low = 0
        high = len(nums)-1
        farthest_right = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                farthest_right = mid
                low = mid + 1  # go left to find earlier occurences
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return [farthest_left, farthest_right]

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,8,8,8,10], 8))