#https://leetcode.com/problems/minimum-path-sum/description/
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
#Note: You can only move either down or right at any point in time.
#
#Example 1:
#[[1,3,1],
# [1,5,1],
# [4,2,1]]
#Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp(i,j): the minimum paths from top left to cur loc
        #dp(i,j) = min(dp(i - 1, j), min(dp(i, j - 1))) + A(i,j)
        
        m, n = len(grid), len(grid[0])
        dp = [[sys.maxsize for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
