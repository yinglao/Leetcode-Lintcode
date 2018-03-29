#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.
#For example,
#
#Consider the following matrix:
#
#[
#  [1,   4,  7, 11, 15],
#  [2,   5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]
#Given target = 5, return true.
#
#Given target = 20, return false.

class Solution:
#T(n) = O(n^(log_2(3)))
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        return self.helper(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
       
    def helper(self, matrix, target, sr, er, sc, ec): # startRow, endRow, startCol, endCol
        
        if er - sr <= 1 and ec - sc <= 1:
            return target in matrix[sr][sc : ec + 1] or target in matrix[er][sc : ec + 1]
        
        mr = sr + (er - sr) // 2
        mc = sc + (ec - sc) // 2
        if matrix[mr][mc] >= target:
            return self.helper(matrix, target, sr, mr, sc, mc) or self.helper(matrix, target, sr, mr, mc, ec) or self.helper(matrix, target, mr, er, sc, mc)
        else:
            return self.helper(matrix, target, mr, er, sc, mc) or self.helper(matrix, target, mr, er, mc, ec) or self.helper(matrix, target, sr, mr, mc, ec) 
        
#这种matrix逆时针旋转45°看就是一棵binary search 的图，左边的neighbor 比root小，右边的neighbor 比root 大。
#利用这种思路，需要仔细考虑越界问题（return false）（60 - 61）
#T(n) = O(m + n)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        x, y = 0, len(matrix[0]) - 1
        
        while not (x == len(matrix) - 1 and y == 0):
            if x > len(matrix) -1 or y < 0:
                return False
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            else:
                x += 1
        return matrix[x][y] == target
    
         
