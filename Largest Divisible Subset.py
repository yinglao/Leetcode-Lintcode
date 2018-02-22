#Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# Notice
#If there are multiple solutions, return any subset is fine.
#
#Have you met this question in a real interview? 
#Example
#Given nums = [1,2,3], return [1,2] or [1,3]
#
#Given nums = [1,2,4,8], return [1,2,4,8]
#http://www.lintcode.com/en/problem/largest-divisible-subset/#
#
#
#先将nums sort
#建立一个全局list dp，第i个数记录nums[i]所在的LDS的个数。
#遍历nums，每次获取nums[i]，将之与nums[i-1], nums[i-2]...逐一比较，直到找到nums[i] % nums[j] == 0, 则dp[i] = dp[j] + 1，如此直到结束，求max(dp)对应的index，k，然后backtrack，使cur = num[k], 碰到nums[k] % nums[x] == 0 的，就让cur = nums[x], 将nums[x] 放进res，继续回溯直至1.
#
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if nums is None:
            return None
        if len(nums) == 0:
            return []
        dummy = [1] + nums
        dummy.sort()
        dp = [0 for i in range(len(dummy))]
        for i in range(1, len(dummy)):
            j = i - 1
            while j >= 1 and dummy[i] % dummy[j] != 0:
                j -= 1
            dp[i] = dp[j] + 1
        k = dp.index(max(dp))
        lds = [dummy[k]]
        large = dummy[k]
        k -= 1
        while k >= 1:
            if large % dummy[k] == 0:
                lds.append(dummy[k])
                large = dummy[k]
            k -= 1
        return lds
            
