class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors2(self, nums):
        # write your code here
        if not nums:
            return None
        count = [0, 0 ,0]
        for num in nums:
            count[num] += 1 
        i = 0
        for num in range(3):
            for j in range(count[num]):
                nums[i] = num
                i += 1
        return nums
            
            
    
        
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return
        pl, pr = 0, len(nums) - 1
        i = 0
        while i != pr:
            if nums[i] == 0:
                self.swap(nums, i, pl)
                i += 1
                pl += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, i, pr)
                pr -= 1
    
    def swap(self, nums, i, j):
        nums[j], nums[i] = nums[i], nums[j]
