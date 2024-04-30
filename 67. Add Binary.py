# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # pad the smaller string with zeroes to make it easier
        if len(a) < len(b):
            a = a.zfill(len(b))
        elif len(b) < len(a):
            b = b.zfill(len(a))
        result = ""
        carry = False
        for bit_a, bit_b in zip(reversed(a), reversed(b)):
            # if either them are one
            if (bit_a == "1") ^ (bit_b == "1"):
                if carry:
                    result = "0" + result
                else:
                    result = "1" + result
            # both are one
            elif bit_a == "1" and bit_b == "1":
                if carry:
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = True
            # both are zero 
            else:
                if carry:
                    result = "1" + result
                    carry = False
                else:
                    result = "0" + result
        # if there is a carry bit at the end
        if carry:
            result = "1" + result
        return result

if __name__ == "__main__":
    solution = Solution()  
    print(solution.addBinary("11", "1"))   
    print(solution.addBinary("1010", "1011"))         