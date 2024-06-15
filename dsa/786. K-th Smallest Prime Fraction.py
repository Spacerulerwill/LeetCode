# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class QuadraticSolution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fractions = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fractions.append((arr[i], arr[j]))
        fractions.sort(key=lambda x: x[0]/ x[1], reverse=True)
        return fractions[-k]

if __name__ == "__main__":
    solution = QuadraticSolution()
    print(solution.kthSmallestPrimeFraction([1,2,3,5], 3))