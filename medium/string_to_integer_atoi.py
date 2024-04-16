# https://leetcode.com/problems/string-to-integer-atoi/description/

INT_MAX = 2**31-1
INT_MIN = -(2**31)

class Solution:
    # cant cheat because python has abritrary length integers
    # must detect overflow before we multiply 
    def myAtoi(self, s: str) -> int:
        # remove trailing and leading whitespace
        s = s.lstrip()
        # if string is empty, we don't care lol
        if len(s) == 0:
            return 0
        # determine sign
        idx = 0
        negative = s[idx] == "-"
        if negative or s[idx] == "+":
            idx += 1
        result = 0
        # we are now at the actual significant numbers
        while idx < len(s):
            char = s[idx]
            # if we find a non digit character, terminate
            if not char.isdigit():
                break
            digit = int(char)
            # check for underflow if negative, overflow if positive
            if negative:
                # multiply by 10, checking for underflow
                if result < INT_MIN // 10:
                    return INT_MIN
                else:
                    result *= 10
                
                # subtract digit, checking for overflow
                if result < INT_MIN + digit:
                    return INT_MIN
                else:
                    result -= digit
            else:
                 # multiply by 10, checking for overflow
                if result > INT_MAX // 10:
                    return INT_MAX
                else:
                    result *= 10
                # add digit, checking for overflow
                if result > INT_MAX - digit:
                    return INT_MAX
                else:
                    result += digit
            idx += 1
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
        