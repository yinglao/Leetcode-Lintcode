#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# Notice
#Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#
#
#Example
#Given the following triangle:
#
#[
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
#]
#The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#http://www.lintcode.com/en/problem/triangle/#
########################################################################################################################

#F(i,j): 到第i行第j个数的的minimum sum path.
#Base cases: F(0,0) = triangle[0][0], F(i,0) = prefixSum(triangle[i][0]), F(i, i) = prefixSum(triangle[i][i])
#Recursion: 
#F(i,j) = min(F(i - 1,j - 1), F(i - 1, j)) + triangle[i][j]
#Goal: min(F[m])
#Implementation 略

#空间复杂度优化：
#F(j): 当前行第j个数的minimum sum path
#Base cases: F(0) = grid[0][0]， F(i) = -1
#recursion：
#第i次迭代，j = i, i - 1, ... 0
#如果F(j)是-1，则 F(j) = F(j - 1) + grid[i][j]
#如果j ==0: 则F(j) = F(j) + grid[i][j]
#否则：F(j) = min(F(j), F(j - 1)) + grid[i][j]
#Goal: min(F)
#T(n) = O(n^2), S(n) = O(n)
########################################################################################################################

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        dp = [-1 for i in range(n)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            j = i - 1
            while j > 0:
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
                j -= 1
            dp[0] = dp[0] + triangle[i][j]
        return min(dp)
