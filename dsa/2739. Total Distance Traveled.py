# https://leetcode.com/problems/total-distance-traveled/description/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_dist = 0
        while mainTank >= 5:
            total_dist += 50
            mainTank -= 5
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        total_dist += mainTank * 10
        return total_dist

if __name__ == "__main__":
    solution = Solution()
    print(solution.distanceTraveled(5, 10))