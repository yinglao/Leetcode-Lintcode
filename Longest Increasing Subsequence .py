#Given a sequence of integers, find the longest increasing subsequence (LIS).
#
#You code should return the length of the LIS.
#
#
#Clarification
#What's the definition of longest increasing subsequence?
#
#The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.
#
#https://en.wikipedia.org/wiki/Longest_increasing_subsequence
#
#Example
#For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
#For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
#
#Challenge 
#Time complexity O(n^2) or O(nlogn)



class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    
#F(i): The LIS ending with nums[i]
#Recursion: 
#F(i) = F(k) + 1, where nums[k] is the first previous element that is smaller than A[i]
#Base case: F(0) =1, []=> 0, None => 0
#Goal: max(F(i) for all i)


    def longestIncreasingSubsequence2(self, nums):
        # write your code here
        
        if not nums: 
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            j = i - 1
            maximum = 0
            while j >= 0:
                if nums[j] < nums[i]:
                    maximum = max(dp[j], maximum)
                j -= 1
            dp[i] = maximum + 1
        return max(dp)
        
#Second Method:
#在已经访问过的数中，第一个不小于当前数的数p 和当前数c 对后面的数而言，作用是一样的：后面的数只要比当前数大，则其对应的lis就应该+1.相当于c将p的效果覆盖了：效果（c）包含效果（p）。
#
#那第二个比当前数大的数q呢？如果后面的数比c大，依然有可能比p和q大，如果c覆盖的是q，则后面的数因为不知道c和p哪个出现更早，从而无法判断该+1还是+2。
#
#第二种做法建立一个新的递增数组minlast，长度比nums大1或以上，（初始化为-inf , inf, inf, ...inf）在遍历nums时，每次都在minlast中找到第一个不小于cur的数，将该数替换成cur，这样以来，每次只在cur比之前遍历的数都要大的时候，才会占据新的inf的位置。如果需要找到其中一个LIS，可以记录下每次新的inf被占据的值。        
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        minlast = [-sys.maxint] + [sys.maxint] * (len(nums))
        for num in nums:
            index = self.bs(minlast, num, 0, len(minlast) - 1)
            minlast[index] = num
        i = 1
        while i <= len(nums) and minlast[i] != sys.maxint:
            i += 1
        return i - 1
        
    def bs(self, minlast, target, si, ei):
        
        while ei > si + 1:
            mi = si + (ei - si) // 2
            if target > minlast[mi]:
                si = mi + 1
            else:
                ei = mi
        return si if minlast[si] > target else ei
        
        
            
        
