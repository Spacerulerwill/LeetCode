# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        num_steps = 0
        
        while not (len(s) == 1 and s[0] == "1"):
            # If the number is odd, add one
            if s[-1] == "1":
                carry = True
                for i in range(len(s) - 1, -1, -1):
                    if s[i] == '1':
                        s[i] = '0'
                    else:
                        s[i] = '1'
                        carry = False
                        break
                if carry:
                    s.insert(0, '1')
            else:
                # i divisible by two, shift right
                s.pop()                
            num_steps += 1
            
        return num_steps
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSteps("1101")) 