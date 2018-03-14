#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Your goal is to reach the last index in the minimum number of jumps.
#
#Have you met this question in a real interview? 
#Example
#Given array A = [2,3,1,1,4]
#
#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)


class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump2(self, A):
        # write your code here
        dp = [sys.maxint for i in range(len(A))]
        dp[0] = 0
        for i in range(1, len(A)):
            for j in range(i):
                if j + A[j] >= i:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]
#动态规划是O(n2)
#
#下面这种方法只要O(n)
#用三个指针i, j,k， i 遍历数组，j记录当前拓展的fringe，k从j + 1出发，扩展新的fringe，当fringe到最后一位时，返回当前值。
#dp[k] = dp[i] + 1         
    def jump(self, A):
        # write your code here
        fringe = 0
        dp = [0 for i in range(len(A))]
        for i in range(len(A)):
            for j in range(fringe + 1, i + A[i] + 1):
                dp[j] = dp[i] + 1
                if j == len(A) - 1:
                    return dp[j]
            fringe = max(j, fringe)
        return -1
