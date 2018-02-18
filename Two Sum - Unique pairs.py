#Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
#
#Have you met this question in a real interview? 
#Example
#Given nums = [1,1,2,45,46,46], target = 47
#return 2
#
#1 + 46 = 47
#2 + 45 = 47
# http://www.lintcode.com/en/problem/two-sum-unique-pairs/#




class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
# 方法一    
#将nums排序
#设立左右两个指针l, r，从两端开始往内筛查
#如果nums[l] + nums[r] = v == target: count ++, 
#l左移至下一个异值数
#r右移至下一个异值数
#如果 v < target, l左移至下一个异值数
#如果v > target, r右移至下一个异值数
#直至l >= r    
    def twoSum6_2(self, nums, target):
        # write your code here
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            print l, r
            s = nums[l] + nums[r]
            if s == target:
                count += 1
                l += 1
                while l <= len(nums) - 1 and nums[l] == nums[l - 1]:
                    l += 1
                r -= 1
                while r >= 0 and nums[r] == nums[r + 1]:
                    r -= 1
            elif s > target:
                r -= 1
                while r >= 0  and nums[r] == nums[r + 1]:
                    r -=1
            else:
                l += 1
                while l <= len(nums) - 1 and nums[l] == nums[l - 1]:
                    l += 1
        return count
        
        
        
#方法二：
#用hashmap来记录数字的使用情况，没有用过的标记为1，有用过的标记为0
#顺序遍历，设当前数为cur，求v = target - cur, 
#如果v 在hashmap中，且值为1， 则count += 1，将haspmap[cur] = 0, hash[v] = 0
#如果v 不在hashmap中，则hash[cur] = 1
#如果v在hashmap中，且值为0， continue

    def twoSum6(self, nums, target):
        # write your code here
        explored = {}
        count = 0
        for num in nums:
            v = target - num
            if v in explored and explored[v] == 1:
                count += 1
                explored[num] = 0
                explored[v] = 0
            elif not v in explored:
                explored[num] = 1
        return count
            
