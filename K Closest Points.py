#Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
#Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.
#
#Have you met this question in a real interview? 
#Example
#Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
#return [[1,1],[2,5],[4,4]]

#建立一个含有k个元素的deque，每个元素是[distance, x, y]， 一开始先将前k个点加进去，后面每加进去一个点的信息，就进行一次排序，再根据排序完的结果,去掉最后一名，如此直至所有点遍历完。
#T(n) = O(nklog(k))
#可以优化成O(nk)




"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        res = []
        x0, y0 = origin.x, origin.y
        for i in range(k):
            x = points[i].x
            y = points[i].y
            distance = ((x - x0)**2 + (y - y0)**2)**0.5
            res.append([distance, x, y])
        for i in range(k,len(points)):
            x = points[i].x
            y = points[i].y
            distance = ((x - x0)**2 + (y - y0)**2)**0.5
            res.append([distance, x, y])
            res.sort()
            res.pop()
        result = []
        for data in res:
            result.append([data[1], data[2]])
        return result
