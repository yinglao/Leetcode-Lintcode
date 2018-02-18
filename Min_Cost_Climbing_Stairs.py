#On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

#Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can #either start from the step with index 0, or the step with index 1.
#Example 1:
#Input: cost = [10, 15, 20]
#Output: 15
#Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
#Example 2:
#Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#Output: 6
#Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
#Note:
#cost will have a length in the range [2, 1000].
#Every cost[i] will be an integer in the range [0, 999].
#https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution:
    #Bottom up
    def minCostClimbingStairs2(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        dp = [-1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        res = min(dp[-1], dp[-2])
        return res
    
    #Top down
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.dp = {}
        self.dp[0], self.dp[1] = cost[0], cost[1]
        return min(self.helper(cost, len(cost) - 1), self.helper(cost, len(cost) - 2))
    
    def helper(self, cost, i):
        if i  <= 1:
            return self.dp[i]
        if i in self.dp:
            return self.dp[i]
        else:
            res = min(self.helper(cost, i - 1), self.helper(cost, i - 2)) + cost[i]
            self.dp[i] = res
        return res
            
