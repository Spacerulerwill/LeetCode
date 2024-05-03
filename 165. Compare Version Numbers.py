# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = [int(revision) for revision in version1.split(".")]
        revisions2 = [int(revision) for revision in version2.split(".")]

        # iterate up two their minimum length
        for idx, (one, two) in enumerate(zip(revisions1, revisions2)):
            if one > two:
                return 1
            if two > one:
                return -1
        
        # if we have any left on either revision, iterate and if we find a non zero it must be bigger
        if idx != len(revisions1) - 1:
            for i in range(idx+1, len(revisions1)):
                if revisions1[i] != 0:
                    return 1
        elif idx != len(revisions2) -1:
            for i in range(idx+1, len(revisions2)):
                if revisions2[i] != 0:
                    return -1
        return 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.compareVersion("1.0.0.0.1", "1"))