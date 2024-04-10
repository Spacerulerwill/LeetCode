class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        smallest = 1
        seen = set()
        for num in nums:
            if num < smallest:
                continue
            if num == smallest:
                while True:
                    smallest += 1
                    if smallest not in seen:
                        break
            else:
                seen.add(num)
        return smallest

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([0,1,2]))