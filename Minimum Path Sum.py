#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Notice
#You can only move either down or right at any point in time.
#
#F(i,j)： 到grid[i][j] 的path with minimum sum
#Base Cases: F(i, 0) = prefixSum(grid[i][0])
#F(0, j) = prefixSum(grid[0][j])
#Recursion: F(i,j) = min(F(i - 1,j), F(i, j - 1)) + grid[i][j]
#Goal: F(m,n)



class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum2(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
        
    
    def minPathSum(self, grid):
        # write your code here  
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        def helper(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = min(helper(i - 1, j), helper(i, j - 1)) + grid[i][j]
            return dp[i][j]
            
        return helper(m - 1, n - 1)
