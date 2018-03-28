# https://leetcode.com/problems/set-matrix-zeroes/description/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# 
# click to show follow up.
# 
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
我们在记录时不能改变未走过的格子，但可以改变已经走过的格子。而每一行和每一列的开头一定是该行和该列最先走的，所以可以利用这一特点设计记录方法。

class Solution:
    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        record = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    record[i][j] = 1
        for i in range(m):
            for j in range(n):
                if record[i][j] == 1:
                    for jj in range(n):
                        matrix[i][jj] = 0
                    for ii in range(m):
                        matrix[ii][j] = 0
        
    def setZeroes3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """       
        m, n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in list(rows):
            for j in range(n):
                matrix[i][j] = 0
        for j in list(cols):
            for i in range(m):
                matrix[i][j] = 0
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """       
        m, n = len(matrix), len(matrix[0])
        row0 = False
        col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        #print(matrix)
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        #print(matrix)
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
