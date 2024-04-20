# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []
        
        out = []
        def backtrack(result:str=""):
            if len(result) == len(digits):
                out.append(result)
                return     
            digit = digits[len(result)] 
            for char in map[digit]:
                backtrack(result + char)
        backtrack()
        return out
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))