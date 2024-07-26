# https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        apples = sum(apple)
        box_count = 0
        i = len(capacity) - 1
        while apples > 0 and i >= 0:
            apples -= capacity[i]
            i -= 1
            box_count += 1
        return box_count

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumBoxes([1,3,2], [4,3,1,5,2]))