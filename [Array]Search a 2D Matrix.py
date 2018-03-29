#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.
#For example,
#
#Consider the following matrix:
#
#[
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
#]
#Given target = 3, return true.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        # search row
        lo, hi = 0, len(matrix) - 1
        while hi - lo > 0:
            mi = lo + (hi - lo) // 2
            if matrix[mi][-1] >= target:
                hi = mi
            else:
                lo = mi + 1
        row = lo
        
        lo, hi = 0, len(matrix[0]) - 1
        while hi - lo > 1:
            mi = lo + (hi - lo) // 2
            if matrix[row][mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return target in matrix[row][lo : hi + 1]
