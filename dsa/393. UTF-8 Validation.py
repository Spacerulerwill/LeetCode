# https://leetcode.com/problems/utf-8-validation/

class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        i = 0
        n = len(data)
        while i < n:
            datum = data[i]
            if datum & 0b10000000 == 0b00000000:
                # 0xxxxxxx: 1-byte character - we skip this loop
                i += 1
                continue
            elif datum & 0b11100000 == 0b11000000:
                # 110xxxxx: 2-byte character
                num_bytes = 1
            elif datum & 0b11110000 == 0b11100000:
                # 1110xxxx: 3-byte character
                num_bytes = 2
            elif datum & 0b11111000 == 0b11110000:
                # 11110xxx: 4-byte character
                num_bytes = 3
            else:
                # if it does not match any of the previous then its invalid
                return False
            # Check if there are enough bytes left for the current UTF-8 character
            if i + num_bytes >= n:
                return False
            # Check the following bytes
            for _ in range(num_bytes):
                i += 1
                if data[i] & 0b11000000 != 0b10000000:
                    return False
            i += 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.validUtf8([197,130,1]))