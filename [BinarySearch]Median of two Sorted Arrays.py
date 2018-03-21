#There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
#
#Have you met this question in a real interview? 
#Example
#Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
#
#Given A=[1,2,3] and B=[4,5], the median is 3.
#
#这是一道看着简单实际上情况很复杂的题目。

#当两个数列的总长度为偶数时，中位数定义为排序后中间两数的平均值，而这两个数的实际位置没有关系，所以我们需要确定两个数列的第k小的数是多少。
#
#首先我们找到A B数列各自的第k//2个数，每次去掉A前面的k//2个数或者B前面的k//2个数。
#这里会遇到一个问题，如果其中一个数列的长度不够k//2怎么办？
#一个巧妙的技巧是假设不够的话，后面全部补上无穷大。也就是说如果发现len(A) - 1 < k//2, candA = sys.maxsize
#每次根据去掉的数的个数来更新k
#
#最后一定会出现k = 1的情况，直接return 两个数组中较小的数。
#
#这里依然用si和ei的移动来实现数组的部分删减。
#
#T(n) = O(log (m + n))

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        totalLength = len(A) + len(B)
        if totalLength == 0:
            return None
        if totalLength % 2 == 1:
            return self.findKth(A, B, totalLength // 2 + 1)
        else:
            return 0.5 * (self.findKth(A, B, totalLength // 2) + self.findKth(A, B, totalLength//2+ 1))
    
    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        siA, siB, eiA, eiB = 0, 0, len(A) - 1, len(B) - 1
        while k != 1:
            candA = A[siA + k//2 - 1] if k//2 <= eiA + 1 - siA else sys.maxsize 
            candB = B[siB + k//2 - 1] if k//2 <= eiB + 1 - siB else sys.maxsize 
            if candA > candB:
                siB = siB + k//2
            else:
                siA = siA + k//2
            k = k - k//2
        a = A[siA] if siA <= eiA else sys.maxsize
        b = B[siB] if siB <= eiB else sys.maxsize
        return a if a <= b else b
