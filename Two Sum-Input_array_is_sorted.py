# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# 
#  Notice
# You may assume that each input would have exactly one solution.
# 
# 
# Example
# Given nums = [2, 7, 11, 15], target = 9
# return [1, 2]

# 用两根指针pl， pr，从头尾开始遍历，令 S = A[pl] +A[pr]
# 如果：
# S == target, return pl, pr;
# S > target, 说明右边的数太大，pr--；
# S < target, 说明左边的数太小，pl ++;
# 至 pr == pl 时结束
# 


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        pl, pr = 0, len(nums) - 1
        while pl < pr:
            s = nums[pl] + nums[pr]
            if s == target:
                return pl + 1, pr + 1
            elif s < target:
                pl += 1
            else:
                pr -= 1
        return None
