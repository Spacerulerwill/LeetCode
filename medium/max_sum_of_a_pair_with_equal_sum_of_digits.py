class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        seen = {}
        _max = -1
        for num in nums:
            num_save = num
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            if digit_sum in seen:
                potential_new_max = num_save + seen[digit_sum]
                _max = max(_max, potential_new_max)
                seen[digit_sum] = max(num_save, seen[digit_sum])
            else:
                seen[digit_sum] = num_save
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSum([18, 43, 36, 13, 7]))