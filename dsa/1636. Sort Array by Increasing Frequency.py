# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from collections import defaultdict

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # counting sort in ascending order 
        _min = min(nums)
        _max = max(nums)
        num_counts = defaultdict(lambda: 0)
        for num in nums:
            num_counts[num] += 1
        ascending = nums[:]
        j = 0
        for i in range(_min, _max+1):
            for _ in range(num_counts.get(i, 0)):
                ascending[j] = i
                j += 1
        # retake counts using ascending order
        num_counts = defaultdict(lambda: 0)
        for num in ascending:
            num_counts[num] += 1
        # create frequency table
        freq_table = defaultdict(lambda: [])
        for num, count in num_counts.items():
            freq_table[count].append(num)
        # sort the frequency table
        _max = max(freq_table.keys())
        _min = min(freq_table.keys())
        new_freq_table = {}
        j = 0
        for i in range(_min, _max+1):
            get = freq_table.get(i)
            if get is not None:
                new_freq_table[i] = get
        # construct final array
        j = 0
        for count, new_nums in new_freq_table.items():
            for num in reversed(new_nums):
                for _ in range(count):
                    nums[j] = num
                    j += 1
        return nums
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.frequencySort([1,1,2,2,2,3]))
    #print(solution.frequencySort([2,3,1,3,2]))