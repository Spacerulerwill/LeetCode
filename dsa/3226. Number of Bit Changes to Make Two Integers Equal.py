# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

# O(n) time O(1) space
class Solution1:
    def minChanges(self, n: int, k: int) -> int:
        min_changes = 0
        while n != 0 or k != 0:
            n_bit = n & 1
            k_bit = k & 1
            # impossible to make equal
            if k_bit == 1 and n_bit == 0:
                return -1
            elif n_bit == 1 and k_bit == 0:
                min_changes += 1
            n >>= 1
            k >>= 1
        return min_changes
    
# O(1) time O(1) space
class Solution2:
    def minChanges(self, n: int, k: int) -> int:
        bit_differences = n ^ k
        if bit_differences & k != 0:
            return -1
        return bit_differences.bit_count()

if __name__ == "__main__":
    solution1 = Solution1()
    print(solution1.minChanges(13, 4))
    solution2 = Solution2()
    print(solution2.minChanges(13, 4))
    