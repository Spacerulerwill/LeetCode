# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        values = list(zip(names, heights))
        values.sort(key=lambda x: x[1], reverse=True)
        return [value[0] for value in values]

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))