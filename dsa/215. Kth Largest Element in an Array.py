# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        
        heapq.heapify(nums)
        for _ in range(k):
            k = heapq.heappop(nums)
        return k * -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([3,2,1,5,6,4], 2))