#A robot is located at the top-left corner of a m x n grid.
#
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
#
#How many possible unique paths are there?
#
# Notice
#m and n will be at most 100.
#
#
#Example
#Given m = 3 and n = 3, return 6.
#Given m = 4 and n = 5, return 35.
#http://www.lintcode.com/en/problem/unique-paths/#
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    
#Bottom up
#F(i, j) : （以终点为（m - 1，n -1），往右一格j ++，往下一格i ++）从给定位置(i, j)到终点的unique path 的数量
#
#Goal: F(0,0)
#
#BaseCase: F(m -1,n - 1) = 1, F(i, n -1) = F(m - 1,j) = 1,i = 0,1,2,.. m - 1, j = 0,1,2,...,n - 1;
#
#Recursion: F(i,j) = F(i + 1, j) + F(i, j + 1)
    def uniquePaths2(self, m, n):
        # write your code here
        dp = [[-1] * n] * m
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[m - 1 - i][n - 1 - j] = dp[m - i][n - 1 - j] + dp[m - 1 - i][n - j]
        return dp[0][0]
#Top down with memorization:
#建一个字典作为全局变量，记录计算过的F(i, j)。将F(m - 1,j) = 1和F(i, n - 1) = 1先放进去，建立一个helper function，参数是i,j, 返回F(i,j), basecase是d(i,j)存在时，直接返回，否则返回Recursion 方程。                
    def uniquePaths(self, m, n):
        # write your code here
        d = {}
        for i in range(m):
            d[(i, n - 1)] = 1
        for j in range(n):
            d[(m - 1, j)] = 1
        def helper(i, j):
            if (i, j) in d:
                return d[(i, j)]
            else:
                val = helper(i + 1, j) + helper(i, j + 1)
                d[(i,j)] = val
                return val
        return helper(0, 0)
         
