#Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
#Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
#A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
#http://www.lintcode.com/en/problem/sort-colors-ii/

# 方法一：数一下每种color各有多少个，然后重新填colors中各个元素。
# T(n) = O(n), S(n) = O(k)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors22(self, colors, k):
        # write your code here
        if not colors:
            return
        count = [0] * (k + 1)
        for color in colors:
            count[color] += 1
        i = 0
        for color in range(1, k + 1):
            for time in range(count[color]):
                colors[i] = color
                i += 1
                
                
                
# 方法二：利用两个指针，每次遍历colors，将当前区间的最大值和最小值分别排到最前面和最后面，相当于完成了两种颜色的排序，然后更新区间范围，进入下一轮遍历。
# T(n) = O(nk), S(n) = O(1)
    def sortColors23(self, colors, k):
        # write your code here
        if not colors:
            return
        
        left, right = 0, len(colors) - 1
        while left < right:
            l, r = left, right
            maximum, minimum = 0, k + 1
            for i in range(l, r + 1):
                maximum = max(colors[i], maximum)
                minimum = min(colors[i], minimum)
            cur = l
            while cur <= r:
                if colors[cur] == minimum:
                    self.swap(colors, cur, l)
                    l += 1
                    cur += 1
                elif colors[cur] == maximum:
                    self.swap(colors, cur, r)
                    r -= 1
                else: 
                    cur += 1
            left = l
            right = r 
            
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
   

# 方法三：Divide and Conquer
# 设计一个helper 函数将colors 分成两部分，左边的颜色数小于或等于k//2, 右边的颜色数大于k//2. 然后对左右两部分各自apply helper函数。
# helper函数的实现：利用左右两个指针l, r，当colors[l] > k//2, 交换左右指针对应的值，r--; 当color[l] <= k//2, l++
# T(n) = nlog(k), S(n) = O(1)
    def sortColors2(self, colors, k):
        # write your code here
        self.helper(colors, 0, len(colors) - 1, 1, k)
        
    def helper(self, colors, startIndex, endIndex, colorFrom, colorTo):
        if colorTo == colorFrom:
            return 
        midColor = colorFrom + (colorTo - colorFrom) // 2
        l, r = startIndex, endIndex
        while l <= r:
            #print l, r
            if colors[l] <= midColor:
                l += 1
            elif colors[l] > midColor:
                self.swap(colors, l, r)
                r -= 1
            #print colors
        self.helper(colors, startIndex, l - 1, colorFrom, midColor)
        self.helper(colors, l, endIndex, midColor + 1, colorTo)
