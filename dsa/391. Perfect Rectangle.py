# https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        # if it does make a whole rectangle, the area is from the min and max x and y coords
        min_x = min(min(rectangle[0], rectangle[2]) for rectangle in rectangles)
        max_x = max(max(rectangle[0], rectangle[2]) for rectangle in rectangles)
        min_y = min(min(rectangle[1], rectangle[3]) for rectangle in rectangles)
        max_y = max(max(rectangle[1], rectangle[3]) for rectangle in rectangles) 
        whole_rect_corners = {(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)}        
        area_of_whole_rectangle = abs((max_x - min_x) * (max_y - min_y))
        # get sum of area of all the individual rectangles
        individual_rectangle_sum = sum(abs((rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])) for rectangle in rectangles)
        # if they don't match it cant be a rectangle cover
        if area_of_whole_rectangle != individual_rectangle_sum:
            return False
        # all rectangle corners apart from the larger rect corner should appear twice
        # the corenrs of the larger rectangle should appear once
        corner_counts = {}        
        for rectangle in rectangles:
            corners = [
                (rectangle[0], rectangle[1]),
                (rectangle[2], rectangle[1]),
                (rectangle[2], rectangle[3]),
                (rectangle[0], rectangle[3])
            ]
            for corner in corners:
                if corner in corner_counts:
                    corner_counts[corner] += 1
                else:
                    corner_counts[corner] = 1
        # check appear twice
        for corner, count in corner_counts.items():
            if corner in whole_rect_corners:
                if count != 1:
                    return False
            else:
                if count % 2 != 0:
                    return False
        # check larger appear once
        for corner in whole_rect_corners:
            if corner_counts.get(corner, 0) != 1:
                return False
        # we got here! success :)
        return True
        



if __name__ == "__main__":
    solution = Solution()
    print(solution.isRectangleCover([[0,0,1,1],[0,0,1,1],[1,1,2,2],[1,1,2,2]]))