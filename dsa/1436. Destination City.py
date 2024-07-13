# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        keys = set(path[0] for path in paths)
        for path in paths:
            destination = path[1]
            if destination not in keys:
                return destination

if __name__ == "__main__":
    solution = Solution()