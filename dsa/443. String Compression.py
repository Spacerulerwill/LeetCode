# vhttps://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: list[str]) -> int:
        idx = 0
        i = 0
        while i < len(chars):
            count = 0
            char= chars[i]
            while i < len(chars)-1 and chars[i] == chars[i+1]:
                i += 1
                count += 1
            count += 1
            i += 1
            if count == 1:
                chars[idx] = char
                idx += 1
            else:
                chars[idx] = char
                idx += 1
                str_count = str(count)
                for ch in str_count:
                    chars[idx] = ch
                    idx += 1
        return idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))