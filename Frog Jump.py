#A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
#Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
#
#If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
#
# Notice
#The number of stones is ≥ 2 and is < 1100.
#Each stone's position will be a non-negative integer < 2^31.
#The first stone's position is always 0.
#Have you met this question in a real interview? 
#Example
#Given stones = [0,1,3,5,6,8,12,17]
#
#There are a total of 8 stones.
#The first stone at the 0th unit, second stone at the 1st unit,
#third stone at the 3rd unit, and so on...
#The last stone at the 17th unit.
#
#Return true. The frog can jump to the last stone by jumping 
#1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
#2 units to the 4th stone, then 3 units to the 6th stone, 
#4 units to the 7th stone, and 5 units to the 8th stone.
#
#Given stones = `[0,1,2,3,4,8,9,11]`
#
#Return false. There is no way to jump to the last stone as 
#the gap between the 5th and 6th stone is too large.



class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
#F(i, j):如果可以， 从第i格跳到第j格用的步数（j-i）,如果不能跳，则为-1
#F(i, j) = j - i if F(i-k, i) == j - i or j - i - 1 or j - i + 1 else -1
#Basecase: F(0, 1) = 1, F(0, j) = -1
#Goal: any(F(i, -1))
#T(n) = O(n**3)


    def canCross2(self, stones):
        # write your code here
        if len(stones) < 2:
            return True
        dp = [[-1 for i in range(len(stones))] for j in range(len(stones))]
        dp[0][1] = 1
        for j in range(len(stones)):
            for i in range(1, j):
                for k in range(i):
                    if dp[k][i] != -1 and self.isNeighbor(dp[k][i], stones[j] - stones[i]):
                        dp[i][j] = stones[j] - stones[i]
                        break
        for i in range(1, len(stones)):
            if dp[i][-1] != -1:
                return True
        return False
    
    def isNeighbor(self, n, m):
        return n == m - 1 or n == m or n == m + 1
        
#仿照跳格子的那道题目，希望可以将时间复杂度简化到O(n**2)

    def canCross(self, stones):
        if len(stones) < 2:
            return True
        d = {}
        for key, value in enumerate(stones):
            d[value] = key
        dp = [[-1 for i in range(len(stones))] for j in range(len(stones))]
        dp[0][1] = 1
        for j in range(1, len(stones)):
            for i in range(j):
                if dp[i][j] != -1:
                    for step in [dp[i][j] - 1, dp[i][j], dp[i][j] + 1]:
                        if step > 0 and stones[j] + step in d:
                            dp[j][d[stones[j] + step]] = step
                        if stones[j] + step == stones[-1] and dp[j][d[stones[j] + step]] != -1:
                            return True
        return False
                    
