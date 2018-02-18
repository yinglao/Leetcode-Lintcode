#Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
#
#All elements < k are moved to the left
#All elements >= k are moved to the right
#Return the partitioning index, i.e the first index i nums[i] >= k.
#
# Notice
#You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
#
#If all elements in nums are smaller than k, then return nums.length

#Example
#If nums = [3,2,2,1] and k=2, a valid answer is 1.
#http://www.lintcode.com/en/problem/partition-array/#




class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
#quickSort 中的partition操作：
#设立两个指针，一个指向第一个大于或等于k的数（待替换），另外一个遍历数组, 当碰到小于k 的数时就swap一下。    
#T(n) = O(n), S(n) = O(1)    
    
    def partitionArray2(self, nums, k):
        # write your code here
        pl = 0
        for i in range(len(nums)):
            if nums[i] < k:
                self.swap(nums, pl, i)
                pl += 1
        return pl
        
    def swap(self, nums, pl, i):
        nums[pl], nums[i] = nums[i], nums[pl]

#分治法：
#处理两段已经partition好的数列，从右半部分的pr = k - 1和左半部分的pl = k 分别往后和往前，逐个替换，直到pl大于middleIndex 或者pr 小于等于middleIndex
#Basecase: endIndex = startIndex, 如果该元素>=k，return startIndex，否则return startIndex + 1
#T(n) = O(nlog(n)), S(n) = O(1)


    def partitionArray(self, nums, k):
        # write your code here
        if not nums or len(nums) == 0:
            return 0
        return self.helper(nums, k, 0, len(nums) - 1)
        
    def helper(self, nums, k, si, ei):
        
        if si == ei:
            return  si if nums[si] >= k else si + 1
        mi = si + (ei - si) // 2
        pl = self.helper(nums, k, si, mi)
        pr = self.helper(nums, k, mi + 1, ei) - 1
        #print pl, pr
        while pl <= mi and pr > mi:
            self.swap(nums, pl, pr)
            pl += 1
            pr -= 1
        return pr + 1 if pl > mi else pl
