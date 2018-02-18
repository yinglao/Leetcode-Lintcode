#Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
#
#Return the difference between the sum of the two integers and the target.
#
#Example
#Given array nums = [-1, 2, 1, -4], and target = 4.
#
#The minimum difference is 1. (4 - (2 + 1) = 1).
#http://www.lintcode.com/en/problem/two-sum-closest-to-target/#




class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
#将nums 排序
#采用左右两个指针l,r, 
#计算 v = nums[l] + nums[r] - target， 如果是0， 直接return 0，否则minimum = min(abs(v - target), minimum)
#如果v > 0，说明若l 右移，所得的数只会离target越远，故r--
#如果v < 0, 说明若r左移， 所得的数只会离target越远，故l ++
#直至l >= r
#T(n) = O(nlog(n)), S(n) = O(1)
    
    
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        l, r = 0, len(nums) - 1
        minimum = sys.maxint
        while l < r:
            v = nums[l] + nums[r] - target
            minimum = min(minimum, abs(v))
            if v == 0:
                return 0
            elif v > 0:
                r -= 1
            else:
                l += 1
        return minimum
