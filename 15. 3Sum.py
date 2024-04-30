# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            # avoid duplicate, don't do anything if same as previous
            if idx > 0 and num == nums[idx-1]:
                continue
            low = idx + 1
            high = len(nums) - 1
            while low < high:
                sum = num + nums[low] + nums[high]
                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
                else:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    # advance low pointer until new number
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
        return res
    
if __name__ == "__main__":
    solution = Solution()
    #print(solution.threeSum([1,-1,-1,0]))
    print(solution.threeSum([0,0,0]))
    print(solution.threeSum([-1,0,1,2,-1,-4]))