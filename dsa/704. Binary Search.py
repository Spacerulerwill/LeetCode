class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))
    print(solution.search([-1,0,3,5,9,12], 2))