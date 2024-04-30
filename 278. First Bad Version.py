# https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            is_mid_bad_version = isBadVersion(mid)
            is_mid_sub_one_bad_version = isBadVersion(mid - 1)
            if is_mid_bad_version and not is_mid_sub_one_bad_version:
                return mid
            if is_mid_bad_version and is_mid_sub_one_bad_version:
                high = mid - 1
                continue
            if not is_mid_bad_version:
                low = mid + 1
                continue