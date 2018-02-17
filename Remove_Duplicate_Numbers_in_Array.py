# Given an array of integers, remove the duplicate numbers in it.
# 
# You should:
# 1. Do it in place in the array.
# 2. Move the unique numbers to the front of the array.
# 3. Return the total number of the unique numbers.
# 
# Example
# Given nums = [1,3,1,4,4,2], you should:
# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

# http://www.lintcode.com/en/problem/remove-duplicate-numbers-in-array/#

class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    #建立一个set explored记录已经访问过的值
    #用两根指针，一个pl指向已经排好的序列的下一个数（待排列的数），另外一个cur用于遍历整个序列。
    #当发现A[cur] not in explored时，swap（A, cur, pl）, pl ++, cur ++, (注意这里cur++ 是因为原来pl所指的元素必然是已经重复的元素，除了一开始。)否则cur++
    #最后返回explored的长度即可
    
    
    def deduplication2(self, nums):
        # write your code here
        explored = set()
        pl, cur = 0, 0
        
        while cur < len(nums):
            if not nums[cur] in explored:
                explored.add(nums[cur])
                self.swap(nums, pl, cur)
                pl += 1
            cur += 1
        return len(explored)
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
#方法二：
#排序；然后设一个最大值，初始化为负无穷，一个count记录当前unique element的个数，初始化为0；然后用两根指针，一个pl指向已经排好的序列的下一个数（待排列的数），另外一个cur用于遍历整个序列。
#当发现A[cur] 比max大时，swap（A, cur, pl）, pl ++, cur ++, (注意这里cur++ 是因为原来pl所指的元素必然是已经重复的元素，除了一开始。)，更新最大值;否则只cur++     

    def deduplication(self, nums):
        # write your code here
        nums.sort()
        cur, pl = 0, 0
        count = 0
        max = - sys.maxint
        while cur < len(nums):
            if nums[cur] > max:
                max = nums[cur]
                self.swap(nums, cur, pl)
                pl += 1
                count += 1
            cur += 1
        return count
