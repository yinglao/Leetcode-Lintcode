#Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
#Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
#A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
#


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
