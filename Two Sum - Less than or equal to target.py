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
#先将nums 排序
#然后设立左右两个指针l, r
#如果nums[l] + nums[r] = v > target: 意味着r前所有的l都会使v > target， 所以使l--
#若v <= target: 意味着所有的l前所有的r都会使v <= target， 所以count += r - l (包括l+1, l+2, ... , r), 然后 l ++



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
