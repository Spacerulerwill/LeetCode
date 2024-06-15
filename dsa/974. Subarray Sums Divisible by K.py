# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_map = {0: 1}
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            # only positive modulos
            if remainder < 0:
                remainder += k
            if remainder in remainder_map:
                count += remainder_map[remainder]
                remainder_map[remainder] += 1
            else:
                remainder_map[remainder] = 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraysDivByK([4,5,0,-2,-3,1], 5))