# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        k = {}
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            if sorted_elem in k:
                k[sorted_elem].append(elem)
            else:
                k[sorted_elem] = [elem]
        
        return list(k.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
