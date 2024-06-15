# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # initial 
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        _max = sum
        left = 0
        right = k - 1
        for i in range(len(nums)-k):
            sum -= nums[left]
            left += 1
            right += 1
            sum += nums[right]
            _max = max(_max, sum)
        return _max / k

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))