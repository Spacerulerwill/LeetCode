# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        # no elements or group size of 1 always possible
        if len(nums) == 0 or k == 1:
            return True
        # if we cant evenly split into groups
        if len(nums) % k != 0:
            return False
        count = Counter(nums)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                for i in range(key, key + k):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPossibleDivide([1,2,3,3,4,4,5,6], 4))