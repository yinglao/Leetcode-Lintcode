#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
#Find the minimum element.
#
# Notice
#You may assume no duplicate exists in the array.
#
#Have you met this question in a real interview? 
#Example
#Given [4, 5, 6, 7, 0, 1, 2] return 0

class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        l, r = 0, len(nums) - 1
        if nums[r] > nums[l]:
            return nums[l]
        while r - l > 1:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        return nums[r]
