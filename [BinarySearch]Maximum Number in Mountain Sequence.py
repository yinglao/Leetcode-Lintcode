下面是三个时期的version，思路都是用二分法，但能够把握问题实质（local judge standard），形成套路模板的代码明显更加短。

class Solution:
    """
    @param: nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence2(self, nums):
        # write your code here
        
        def helper(nums, startIndex, endIndex):
            middleIndex = startIndex + (endIndex - startIndex) // 2
            if endIndex - startIndex == 0:
                return nums[startIndex]
            if endIndex - startIndex == 1:
                if nums[startIndex] >= nums[endIndex]:
                    return nums[startIndex]
                else:
                    return nums[endIndex]
            if nums[middleIndex]>= nums[middleIndex - 1] and nums[middleIndex] >= nums[middleIndex + 1]:
                return nums[middleIndex]
            elif nums[middleIndex - 1] <= nums[middleIndex] and nums[middleIndex] <= nums[middleIndex + 1]:
                return helper(nums, middleIndex + 1, endIndex)
            else: # nums[middleIndex - 1] >= nums[middleIndex] and nums[middleIndex] >= nums[middleIndex + 1]
                return helper(nums, startIndex, middleIndex - 1)
        startIndex, endIndex = 0, len(nums) - 1
        return helper(nums, startIndex, endIndex)
        
    def mountainSequence3(self, nums):
        # write your code here
        if len(nums) <= 4:
            return max(nums)
        l ,r = 0 ,len(nums) - 1
        while r - l > 4:
            m = l + (r - l) // 2
            if nums[m] > nums[m - 1] and nums[m] < nums[m + 1]:
                l = m + 1
            elif nums[m] < nums[m - 1] and nums[m] > nums[m + 1]:
                r = m - 1
            else:
                return nums[m]
        print [nums[l], nums[l + 1], nums[r - 1], nums[r]]
        return max([nums[l], nums[l + 1], nums[r - 1], nums[r]])
        
    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return None
        l, r = 0, len(nums) - 1
        while r - l > 1:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else: 
                l = m + 1
        return max([nums[l], nums[r]])
    
        
