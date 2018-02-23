#Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.
#
# Notice
#It's guaranteed that the size of the array is greater or equal to k.
#
#Have you met this question in a real interview? 
#Example
#Given nums = [1, 12, -5, -6, 50, 3], k = 3
#
#Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
#http://www.lintcode.com/en/problem/maximum-average-subarray/#





class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
#假设nums前面带0， 先求prefix Sum P，前面带0，此时S(j,i) = P[i] - P[j -1], 且nums[i] = S(i,i) = P[s] - P[s - 1].
#
#初始化前k个数的平均值：ave = P[k]/k, 
#初始化目标值res = ave
#i = k
#j = 1
#i ++, 更新平均值 ave = (P[i] - P[j - 1])/(i - j + 1)
#求S(j,j) = P[j] - P[j -1], 如果小于ave，则j ++, 更新平均值，直到S(j,j) 大于平均值或者j == i - k + 1为止，更新res。
#如此直到i = len(P) - 1, 返回res
#以上做法是O(n^2)，本质上跟逐段取没有什么差别。

    def maxAverage2(self, nums, k):
        # write your code here
        if len(nums) < k or not nums:
            return None
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
        #print prefix
        j = 1
        ave = 1.0 * prefix[k] / k
        res = ave
        for i in range(k + 1, len(prefix)):
            ave = 1.0 * (prefix[i] - prefix[j - 1]) / (i - j + 1)
            #m = j
            #while m < i - k + 1:
            #    preAve = 1.0 * (prefix[m] - prefix[j - 1]) / (m - j + 1)
            #    if preAve <= ave: 
            #        j = m + 1
            #        ave = 1.0 * (prefix[i] - prefix[j - 1]) / (i - j + 1)
            #    m += 1
            m = i - k
            while m >= j:
                preAve = 1.0 * (prefix[m] - prefix[j - 1]) / (m - j + 1)
                if preAve <= ave:
                    j = m + 1
                    ave = 1.0 * (prefix[i] - prefix[j - 1]) / (i - j + 1)
                    m = i - k
                m -= 1
            res = max(res, ave)
            #print i, res
        return res
        
        
        
下面利用二分法来做，这种方法对range进行二分，将range调到误差允许范围内，所以得到的并不是准确值，也无法进行backtrack获得具体的对应子数列。

基本思路是先求出nums中的最大值，最小值和中间值，判断其长度>=k的连续子数列最大平均值是否比中间值大，根据结果调整range和mid

判断过程如下，假设目标子数列如下：
A[i+1] + A[i+2]... + A[i+j]/(j - i) <= Mid
<=> A[i+1] - Mid + A[i+2] - Mid... + A[i+j] -Mid <= 0
即构造新数组B，其中B[i] = A[i] - Mid，
原问题转化为数组B中最大（长度大于k的）子序列之和是否大于0.

这是一个O(n)的问题，解决如下：
求B的prefix sum， 前面加0，然后从i = k 往后遍历，每次更新 i - k 及以前的数中的最小值minimum，和最大差值maxdiff。初始化minimum 为正无穷, maxdiff为正无穷。

此处为了通过online Judge，必须在判断maxdiff > 0 后马上进行range的调整（而不能等完全确定maxdiff后）     
T(n) = O(n * log((max - min) / error))

    def maxAverage(self, nums, k):
        # write your code here
        
        upper = max(nums)
        lower = min(nums)
        
        while upper - lower > 5 * 1e-5:
            mid = (upper + lower) / 2.0
            
            ps = [0]
            minimum = float('inf')
            maxdiff = -float('inf')
            check = False
            for i in xrange(1, len(nums) + 1):
                ps.append(ps[-1] + nums[i-1] - mid)
                if i >= k:
                    minimum = min(minimum, ps[i - k])
                    maxdiff = max(maxdiff, ps[i] - minimum)
                if maxdiff >= 0:
                    check = True
                    break
            if check:
                lower = mid
            else:
                upper = mid
        return lower
