# https://leetcode.com/problemset/

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        numRescueBoats = 0
        people.sort()
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[right] == limit:
                right -= 1
            elif people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            numRescueBoats += 1
        return numRescueBoats 

if __name__ == "__main__":
    solution = Solution()
    print(solution.numRescueBoats([3,2,2,1], 3))