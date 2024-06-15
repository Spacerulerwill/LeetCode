# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        left_to_place = n
        while i < len(flowerbed) and left_to_place > 0:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    left_to_place -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        return left_to_place == 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([1,0,0,0,1], 1))
    print(solution.canPlaceFlowers([1,0,0,0,1], 2))
    print(solution.canPlaceFlowers([0,0,1,0,0], 1))