# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            
            right_lower = mid == len(nums)-1 or nums[mid+1] < nums[mid]
            left_lower = mid == 0 or nums[mid-1] <  nums[mid]

            if right_lower and left_lower:
                return mid
            elif not left_lower:
                high = mid - 1
            else:
                low = mid + 1   
          
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1]))