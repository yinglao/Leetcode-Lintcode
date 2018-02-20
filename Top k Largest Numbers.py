#Given an integer array, find the top k largest numbers in it.
#
#
#Example
#Given [3,10,1000,-99,4,100] and k = 3.
#Return [1000, 100, 10].
#http://www.lintcode.com/en/problem/top-k-largest-numbers/#

#将nums heapify, 然后pop k 次，放入到结果数组中。
#T(n) = O(n), S(n) = O(1)



class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        for i in range(len(nums)):
            nums[i] = -nums[i]
        import heapq
        heapq.heapify(nums)
        res = []
        for i in range(k):
            res.append(- heapq.heappop(nums))
        return res
