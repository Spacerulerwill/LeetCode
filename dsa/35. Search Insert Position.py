# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # search for the element
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        # if we can't find - low is insert position
        return low

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 2))
    print(solution.searchInsert([1,3,5,6], 8))