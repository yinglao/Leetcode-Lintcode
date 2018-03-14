#You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
#
#What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
#Have you met this question in a real interview? 
#Example
#Given envelopes = [[5,4],[6,4],[6,7],[2,3]], 
#the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).



class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes2(self, envelopes):
        # write your code here
        envelopes.sort()
        dp = [1 for i in range(len(envelopes))]
        for i in range(1, len(envelopes)):
            wi, hi = envelopes[i]
            for j in range(i):
                wj, hj = envelopes[j]
                if wi > wj and hi > hj:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
        
##这题用dp来解是O(n^2)
#但认真观察可以发现其实是在求LIS，只是这里"increasing"的定义是w2 > w1 and h2 > h1. 而且存在w2 > w1 而 h2 < h1的情况不好进行替换（2不包含于1， 也不包含1）。
#
#一种巧妙的做法是，先将envelopes按w的升序排。如果w相同，则按h的降序排。这样我们只需要找h的LIS。        
        
    
    def maxEnvelopes(self, envelopes):
        # write your code here
        envelopes.sort(key = lambda (x, y): [x, -y])
        hlis = [sys.maxint for i in range(len(envelopes) + 1)]
        for [w, h] in envelopes:
            i = self.bsRight(hlis, h) # Find the first index in hlis that hlis[index] >= h
            hlis[i] = h
        return hlis.index(sys.maxint)
        
    def bsRight(self, hlis, h):
        si = 0
        ei = len(hlis) - 1
        while ei - si > 1:
            mi = si + (ei - si) // 2
            if hlis[mi] < h:
                si = mi + 1
            elif hlis[mi] >= h:
                ei = mi
        return si if hlis[si] >= h else ei
