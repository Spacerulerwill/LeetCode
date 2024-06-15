# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        sorted_idx = 0
        _idx = 0
        while _idx < len(nums):
            current = nums[_idx]
            nums[sorted_idx] = current
            sorted_idx += 1
            if _idx < len(nums) - 1 and nums[_idx + 1] == current:
                nums[sorted_idx] = current
                sorted_idx += 1
            while _idx < len(nums) and nums[_idx] == current:
                _idx += 1
        return sorted_idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,1,2,2,3]))