# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([4,5,6,7,0,1,2]))