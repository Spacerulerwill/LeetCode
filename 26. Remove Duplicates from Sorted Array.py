# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 0
        for _idx, num in enumerate(nums):
            if _idx > 0:
                if num != nums[_idx - 1]:
                    nums[idx] = num
                    idx += 1
            else:
                nums[idx] = num
                idx += 1
        return idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,2,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))