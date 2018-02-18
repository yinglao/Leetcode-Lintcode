#Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.
#
#
#Example
#Given nums = [2, 7, 11, 15], target = 24. 
#Return 5. 
#2 + 7 < 24
#2 + 11 < 24
#2 + 15 < 24
#7 + 11 < 24
#7 + 15 < 25
#http://www.lintcode.com/en/problem/two-sum-less-than-or-equal-to-target/#




class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            v = nums[l] + nums[r]
            if v > target:
                r -= 1
            else:
                count += r - l
                l += 1
        return count
