# https://leetcode.com/problems/climbing-stairs/description/

# Using memoization and depth first traversing a decision tree
class Solution1:
    def climbStairs(self, n: int) -> int:
        ways = 0
        cache = {}
        def dfs(current:int=0):
            nonlocal ways
            if current == n:
                ways += 1
                return
            if current > n:
                return
            if current in cache:
                ways += cache[current]
            else:          
                dfs(current + 1)
                dfs(current + 2)
                cache[current] = ways
        dfs()
        return ways
    
# using bottom up dynamic programming
class Solution2:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one 


if __name__ == "__main__":
    solution = Solution2()
    print(solution.climbStairs(38))