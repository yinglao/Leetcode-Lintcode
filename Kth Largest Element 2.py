#Find K-th largest element in an array. and N is much larger than k.
#
# Notice
#You can swap elements in the array
#
#Have you met this question in a real interview? 
#Example
#In array [9,3,2,4,8], the 3rd largest element is 4.
#
#In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.




class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    
#先将nums中的数变成自身的相反数，然后heapify，然后pop k次
#T(n) = O(n + k log(n)), S(n) = O(1)
    def kthLargestElement2_2(self, nums, k):
        # write your code here
        for i in range(len(nums)):
            nums[i] = -nums[i]
        import heapq
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res
#或者直接heapify nums，然后pop len(nums) - k次
#n个数中第k大的数就是第（n + 1 - k）小的数
#T(n) = O(n + (n-k)log(n)), S(n) = O(1)


    def kthLargestElement2(self, nums, k):
        # write your code here
        import heapq
        heapq.heapify(nums)
        for i in range(len(nums) + 1 - k):
            res = heapq.heappop(nums)
        return res
