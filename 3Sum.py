#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice
#Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#
#The solution set must not contain duplicate triplets.
#
#
#Example
#For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
#
#(-1, 0, 1)
#(-1, -1, 2)
# http://www.lintcode.com/en/problem/3sum/#


#两重循环，
#第一重顺序遍历，使target为当前值，
#第二重从当前值的后一个数出发，寻找- target的two sum pairs, 加入到res中.此处为了偷懒不写跳过重复的l和r，用了set去重，因为结果对排序有要求，所以最后利用python的高级排序（排序元素可以是list）再排一下序。
#第一重循环每次都取相异值，保证uniqueness
#T(n) = O(n^2), S(n) = (1)




class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        cur = 0
        res = set()
        while cur <= len(numbers) - 3:
            target = numbers[cur]
            l, r = cur + 1, len(numbers) - 1
            while l < r:
                v = numbers[l] + numbers[r]
                if v == -target :
                    res.add((target, numbers[l], numbers[r]))
                    l += 1
                    r -= 1
                elif v  < -target:
                    l += 1
                else:
                    r -= 1
            cur += 1
            while cur <= len(numbers) - 3 and numbers[cur] == numbers[cur - 1]:
                cur += 1
        res = list(res)
        res.sort()
        return res
                
