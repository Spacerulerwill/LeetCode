# https://leetcode.com/problems/number-of-atoms

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        elements = []
        counts = []
        parenthesis = []
        i = 0
        n = len(formula)
        while i < n:  
            if formula[i].isupper():
                if i == n - 1:
                    elements.append(formula[i])
                    counts.append(1)    
                else:
                    if formula[i+1].islower():
                        i += 1
                        elements.append(formula[i-1] + formula[i])
                        if i == n - 1 or not formula[i+1].isdigit():
                            counts.append(1)
                    else:
                        elements.append(formula[i])
                        if not formula[i+1].isdigit():
                            counts.append(1)
                i += 1
            elif formula[i].isdigit():
                digit_string = str(formula[i])
                i += 1
                while i < n and formula[i].isdigit():
                    digit_string += str(formula[i])
                    i += 1
                counts.append(int(digit_string))
            elif formula[i] == "(":
                parenthesis.append(len(elements))
                i += 1
            elif formula[i] == ")":
                open_parenthesis_pos = parenthesis.pop()
                if i < n - 1 and formula[i+1].isdigit():
                    i += 1
                    digit_string = ""
                    while i < n and formula[i].isdigit():
                        digit_string += str(formula[i])
                        i += 1
                    multiplier = int(digit_string)
                    j = len(counts)-1
                    while j >= open_parenthesis_pos:
                        counts[j] *= multiplier
                        j -= 1
                else:
                    i += 1
            else:
                i += 1
        # combine element counts
        count_map = defaultdict(lambda: 0)
        for element, count in zip(elements, counts):
            count_map[element] += count
        # sort keys
        sorted_keys = sorted(count_map.keys())
        sorted_count_map = {key: count_map[key] for key in sorted_keys}
        # construct string
        return "".join(element + (str(count) if count > 1 else "") for element, count in sorted_count_map.items())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countOfAtoms("K4(ON(SO3)2)2"))
    print(solution.countOfAtoms("Mg(OH)2"))
    print(solution.countOfAtoms("Mg(H2O)N"))