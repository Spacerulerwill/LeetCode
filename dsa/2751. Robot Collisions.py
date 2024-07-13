# https://leetcode.com/problems/robot-collisions/

# enum for improved readability
POSITION = 0
HEALTH = 1
DIRECTION = 2
IDX = 3

class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # sort them by positions
        robots = [[position, health, direction, idx] for idx, (position, health, direction) in enumerate(zip(positions, healths, directions))]
        robots.sort(key=lambda robot: robot[0])
        stack = []
        for robot in robots:
            if robot[DIRECTION] == "R" or not stack or stack[-1][DIRECTION] == "L":
                stack.append(robot)
                continue

            if robot[DIRECTION] == "L":
                add_robot = True
                while len(stack) > 0 and stack[-1][DIRECTION] == "R" and add_robot:
                    last_health = stack[-1][HEALTH]
                    if robot[HEALTH] > last_health:
                        stack.pop()
                        robot[HEALTH] -= 1
                    elif last_health > robot[HEALTH]:
                        stack[-1][HEALTH] -= 1
                        add_robot = False
                    else:
                        stack.pop()
                        add_robot = False
        
                if add_robot:
                    stack.append(robot)
        # return the healths in order of original positions
        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]

if __name__ == "__main__":
    solution = Solution()
    print(solution.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))
    print(solution.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))
    print(solution.survivedRobotsHealths([3,47], [46,26], "LR"))