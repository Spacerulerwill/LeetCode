# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        valid_addresses = []
        def backtrack(ip_address:str="", current_num:int=0, idx:int=0, parts:int=0, leading_zero:bool=False):
            if idx == len(s):
                if parts == 3:
                    valid_addresses.append(ip_address)
                return
            num = (current_num * 10) + int(s[idx])

            if idx == 0:
                # First number, start the expression
                backtrack(s[idx], int(s[idx]), idx + 1, 0, s[idx] == "0")
            else:
                if num > 255 or leading_zero:
                    backtrack(ip_address + "." + s[idx], int(s[idx]), idx + 1, parts+1, s[idx] == "0")
                else:
                    backtrack(ip_address + s[idx], num, idx + 1, parts, s[idx-1] == "." and s[idx] == "0")
                    backtrack(ip_address + "." + s[idx], int(s[idx]), idx + 1, parts+1, s[idx] == "0")
        backtrack()
        return valid_addresses

if __name__ == "__main__":
    solution = Solution()
    valid_addresses = solution.restoreIpAddresses("25525511135")
    for address in valid_addresses:
        print(address)
