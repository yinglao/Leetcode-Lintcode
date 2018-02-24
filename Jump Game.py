#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
#
# Notice
#This problem have two method which is Greedy and Dynamic Programming.
#
#The time complexity of Greedy method is O(n).
#
#The time complexity of Dynamic Programming method is O(n^2).
#
#We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
#
#
#Example
#A = [2,3,1,1,4], return true.
#
#A = [3,2,1,0,4], return false.
#http://www.lintcode.com/en/problem/jump-game/#



class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    
#F(i) : 记录第i格能否被到达
#Recursion: if F(i) is true, and A[i] is k, then A[i + 1]... A[i + k] is true. If F(i) is false, then continue
#Base case, F(0) is true
#Goal: F(len(A) - 1)
#
#Bugfree： 最后一次jump的时候有可能jump
#不到最大步数，这时候有可能会导致下标溢出

    def canJump2(self, A):
        # write your code here
        dp = [False for i in range(len(A))]
        dp[0] = True
        for i in range(len(A)):
            if dp[i]:
                k = 1
                while k <= A[i] and k + i <= len(A) - 1:
                    dp[i + k] = True
                    k += 1
        return dp[-1]
        
#方法二
#贪心法基于此假设：如果当前格子可被访问，则其前所有格子都可以被访问。
#
#建立一个set，记录已经访问过的格子数。
#每次都跳最大步数，遇到以下三种情况除外：
#1. 当前格子i 已大于等于len(A) - 1, 此时直接return True。
#2. 当前格子数最大步数k = 0, 此时往前逐格调到一个未访问过的格子
#3. 如果往回访问了所有格子 ,return False    

#T(n) = O(n) 每个格子最多访问一遍， S(n) = O(n)

    def canJump(self, A):
        # write your code here
        close = set()
        i = 0
        while True:
            if i in close:
                i -= 1
                continue
            close.add(i)
            if i >= len(A) - 1:
                return True
            elif i < 0:
                return False
            elif A[i] == 0:
                i -= 1
            else:
                i += A[i]
                
