# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        indices = list(range(len(score))) 
        indices.sort(key=lambda i: score[i], reverse=True)
        if len(indices) == 1:
            score[indices[0]] = "Gold Medal"
        elif len(indices) == 2:
            score[indices[0]] = "Gold Medal"
            score[indices[1]] = "Silver Medal"
        elif len(indices) == 3:
            score[indices[0]] = "Gold Medal"
            score[indices[1]] = "Silver Medal"
            score[indices[2]] = "Bronze Medal"
        else:
            score[indices[0]] = "Gold Medal"
            score[indices[1]] = "Silver Medal"
            score[indices[2]] = "Bronze Medal"
            for i in range(3, len(score)):
                score[indices[i]] = str(i + 1)
        return score

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRelativeRanks([5,4,3,2,1]))