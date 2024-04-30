# https://leetcode.com/problems/validate-ip-address/

import string

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        bytes = queryIP.split(".")
        if len(bytes) == 4:
            for byte in bytes:
                if not byte.isnumeric() or int(byte) > 255 or (byte[0] == "0" and byte != "0"):
                    return "Neither"
            return "IPv4"
        
        hex_pairs = queryIP.split(":")
        if len(hex_pairs) == 8:
            for hex_pair in hex_pairs:
                if len(hex_pair) > 4 or len(hex_pair) == 0 or any(c not in string.hexdigits for c in hex_pair):
                    return "Neither"
            return  "IPv6"
        return "Neither"

if __name__ == "__main__":
    solution = Solution()
    print(solution.validIPAddress("172.16.254.1"))
    print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(solution.validIPAddress("256.256.256.256"))