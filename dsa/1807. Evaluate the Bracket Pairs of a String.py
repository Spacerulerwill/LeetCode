# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        map = {data[0]: data[1] for data in knowledge}
        result = ""
        i = 0
        while i < len(s):
            if s[i] == "(":
                key = ""
                i += 1
                while s[i] != ")":
                    key += s[i] 
                    i += 1
                value = map.get(key)
                if value is None:
                    result += "?"
                else:
                    result += value
            else:
                result += s[i]
            i += 1
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))
    print(solution.evaluate("(a)(a)(a)aaa", [["a","yes"]]))