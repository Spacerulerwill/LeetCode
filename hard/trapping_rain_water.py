# https://leetcode.com/problems/trapping-rain-water/description/
from operator import itemgetter

class Solution:
    def trap(self, height: list[int]) -> int:
        # find the max of the height 
        total = 0
        max_idx, _ = max(enumerate(height), key=itemgetter(1)) 
        cur_max = (height[0], 0)
        for i in range(0, max_idx+1):
            # new maximum found - calcuate new water
            if height[i] >= cur_max[0]:
                for j in range(cur_max[1]+1, i):
                    total += cur_max[0] - height[j]
                cur_max = (height[i], i)
        cur_max = (height[len(height)-1], len(height)-1)
        for i in range(len(height)-1, max_idx-1, -1):
            # new maximum found - calcuate new water
            if height[i] >= cur_max[0]:
                for j in range(cur_max[1], i, -1):
                    total += cur_max[0] - height[j]
                cur_max = (height[i], i)
        return total
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(solution.trap([2,0,2]))