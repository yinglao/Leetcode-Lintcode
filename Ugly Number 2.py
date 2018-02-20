#Ugly number is a number that only have factors 2, 3 and 5.
#
#Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
#
# Notice
#Note that 1 is typically treated as an ugly number.
#
#Have you met this question in a real interview? 
#Example
#If n=9, return 10.
#http://www.lintcode.com/en/problem/ugly-number-ii/#

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    
#先在heap中放1，然后pop出来后，分别乘2，3，5后push进heap，如此操作k次。
#为了避免重复元素放入如3*2 和2 * 3, 设置一个set记录已经在heap中的元素，每次放入新元素前都检查是否在set中，不在的话可以同时push进heap中和加入到set中。
#T(n) = O(nlog(n)), S(n)
    def nthUglyNumber2(self, n):
        # write your code here
        import heapq
        factors = [2,3,5]
        close = set([1])
        hq = [1]
        heapq.heapify([1])
        for i in range(n):
            res = heapq.heappop(hq)
            for factor in factors:
                if not res * factor in close: 
                    heapq.heappush(hq, res * factor)
                    close.add(res * factor)
        return res
#方法二：
#每次只产生下一个丑数， 
#利用三个指针p2, p3, p5，分别指向乘以2,3,5后会比当前最大丑数大的丑数。每次都从这三个乘积中取最小值作为下一个丑数。
#T(n) = O(n), S(n) = O(1)
    def nthUglyNumber(self, n):
        # write your code here
        uglys = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(n - 1):
            while uglys[p2] * 2 <= uglys[-1]:
                p2 += 1
            while uglys[p3] * 3 <= uglys[-1]:
                p3 += 1
            while uglys[p5] * 5 <= uglys[-1]:
                p5 += 1
            uglys.append(min(uglys[p2] * 2, uglys[p3] * 3, uglys[p5] * 5))
            
        return uglys[-1]
