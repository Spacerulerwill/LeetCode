# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        already_mapped = set()
        for s_ch, t_ch in zip(s, t):
            if s_ch in map:
                if map[s_ch] != t_ch:
                    return False
            else:
                if t_ch in already_mapped:
                    return False
                map[s_ch] = t_ch
                already_mapped.add(t_ch)
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("badc", "baba"))