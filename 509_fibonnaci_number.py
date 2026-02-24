class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev_a = 0
        prev_b = 1
        num = prev_a + prev_b
        for i in range(2, n):
            prev_a = prev_b
            prev_b = num
            num = prev_a + prev_b
        return num
