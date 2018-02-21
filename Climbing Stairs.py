#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#Have you met this question in a real interview? 
#Example
#Given an example n=3 , 1+1+1=2+1=1+2=3
#
#return 3
#
#http://www.lintcode.com/en/problem/climbing-stairs/#
#
#F(i): 从第0级阶梯开始有F(i)种方法走到第i级阶梯。
#basecase：F(0) = 0, F(1) = 1
#Recursion: F(i) = F(i -1) + F(i)

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        dp = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
