# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for seat, student in zip(seats, students):
            sum += abs(student - seat)
        return sum
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minMovesToSeat([3,1,5], [2,7,4]))