#Follow up for "Unique Paths":
#
#Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Notice
#m and n will be at most 100.

#Example
#For example,
#There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
#[
#  [0,0,0],
#  [0,1,0],
#  [0,0,0]
#]
#The total number of unique paths is 2
#http://www.lintcode.com/en/problem/unique-paths-ii/#




class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles2(self, obstacleGrid):
        # write your code here
        # bottom up
        
#因为仍然只允许向右或者下走，所以跟1 一样，只是初始化稍有不同，状态转换方程时一样的。
#初始化时，F(m-1, n-1) 仍然是1，然后如果边界上有障碍，则障碍以上或者以左都为0，在初始化dp矩阵时，如果obstacle存在设为0， 否则设为-1.
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for i in range(m)]
        # dp = [[-1] * n] * m 第二次乘实际上是shallow copy，会导致改动一个数导致其所在列会全部改动
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        else:
            dp[m - 1][n - 1] = 1
        i = m - 2
        while i >= 0:
            if obstacleGrid[i][n - 1] == 1:
                dp[i][n - 1] = 0
            else:
                dp[i][n - 1] = dp[i + 1][n - 1]
            i -= 1
        j = n - 2
        while j >= 0:
            if obstacleGrid[m - 1][j] == 1:
                dp[m - 1][j] = 0
            else:
                dp[m - 1][j] = dp[m - 1][j + 1]
            j -= 1
        i = m - 2
        while i >= 0:
            j = n -2
            while j >= 0:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                j -= 1
            i -= 1
        return dp[0][0]
#Top down w/ memorization
#初始化步骤完全一样，然后递归时多写一个判断条件。
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        # top down
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for i in range(m)]
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        else:
            dp[m - 1][n - 1] = 1
        i = m - 2
        while i >= 0:
            if obstacleGrid[i][n - 1] == 1:
                dp[i][n - 1] = 0
            else:
                dp[i][n - 1] = dp[i + 1][n - 1]
            i -= 1
        j = n - 2
        while j >= 0:
            if obstacleGrid[m - 1][j] == 1:
                dp[m - 1][j] = 0
            else:
                dp[m - 1][j] = dp[m - 1][j + 1]
            j -= 1
        def helper(i, j):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = helper(i + 1, j) + helper(i, j + 1)
                return dp[i][j]
                
        return helper(0, 0)
