# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        # calculate sum of elements in range max..=max+k 
        # by sutracting sum of 1..=max-1 from sum of 1..=max+k
        _max = max(nums)
        j = _max+k-1
        o = _max-1
        return ((j * (j + 1)) // 2) - ((o * (o + 1)) // 2)

    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeSum([1,2,3,4,5], 3))