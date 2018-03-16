#Given a target number, a non-negative integer target and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
#
#先用binary search找到一对相邻的数（a,b）指数为（l, r）使得target ∈ [a,b]，然后设置两个指针，分别从这两个数开始，
#if abs(A[l] - target) > abs(A[r] - target):
#res.append(A[r])
#r+=1
#else:
#res.append(A[l])
#l-=1
#当然实际上要进行越界的判断。


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if len(A) < k:
            return None
        if A[0] >= target:
            return A[: k]
        if A[-1] <= target:
            return A[-1:-k-1:-1]
        
        l = self.bsleft(A, target)
        r = l + 1
        res = []
        for i in range(k):
            if l == -1:
                res.append(A[r])
                r += 1
            elif r == len(A):
                res.append(A[l])
                l -= 1
            elif abs(A[l] - target) > abs(A[r] - target):
                res.append(A[r])
                r += 1
            else:
                res.append(A[l])
                l -= 1
        return res
        
        
    def bsleft(self, A, target):
        '''Find the last number that is not larger than k'''
        lo, hi = 0, len(A) - 1
        while hi - lo > 1:
            mi = lo + (hi - lo)//2
            if A[mi] > target:
                hi = mi - 1
            else:
                lo = mi
        return hi if A[hi] <= target else lo
        
