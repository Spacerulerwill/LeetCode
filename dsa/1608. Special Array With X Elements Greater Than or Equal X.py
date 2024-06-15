# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        # sort array
        _max = max(nums)
        buckets = [0 for _ in range(_max+1)]
        for num in nums:
            buckets[num] += 1
        suffix_sums = [0 for _ in range(_max+1)]
        sum = 0
        for i in range(_max, -1, -1):
            sum += buckets[i]
            suffix_sums[i] = sum
        for idx, num in enumerate(suffix_sums):
            if num == idx:
                return idx  
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.specialArray([0,4,3,0,4]))