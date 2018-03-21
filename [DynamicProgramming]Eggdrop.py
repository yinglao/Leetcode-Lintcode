#这是一道看着很难实际上很简单的题

#Version1
#
#There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.
#
#You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
#
#Have you met this question in a real interview? 
#Clarification
#For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor. But in this worst case (k = 10), you have to drop 10 times.
#
#Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst case (for example, k = 9) you have to drop 4 times.
#
#Example
#Given n = 10, return 4.
#Given n = 100, return 14.
#http://www.lintcode.com/en/problem/drop-eggs/


class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = sys.maxsize
            for k in range(1, i):
                dp[i] = min(dp[i], 1 + max(k - 1, dp[i - k]))
        return dp[-1]
        
# Version 2
# 
# There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.
#
#You're given m eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
#
#Have you met this question in a real interview? 
#Example
#Given m = 2, n = 100 return 14
#Given m = 2, n = 36 return 8
# http://www.lintcode.com/en/problem/drop-eggs-ii/


class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        # write your code here
        dp = [[sys.maxsize for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][1] = 1
        for j in range(1, n + 1):
            dp[1][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, j):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[m][n]
            
