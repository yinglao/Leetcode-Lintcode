#Design and implement a TwoSum class. It should support the following operations: add and find.

#add - Add the number to an internal data structure.
#find - Find if there exists any pair of numbers which sum is equal to the value.

#add(1); add(3); add(5);
#find(4) // return true
#find(7) // return false

# http://www.lintcode.com/en/problem/two-sum-data-structure-design/#


# 用dict实现，key是值，value是个数，add时直接调用add方法，find时遍历keys，逐个排查
# add T(n) = O(1); Find T(n) = O(n), S(n) = O(n)

class TwoSum2:
    """
    @param: number: An integer
    @return: nothing
    """
    def __init__(self):
        self.data = {}
    
    def add(self, number):
        # write your code here
        self.data[number] = self.data.get(number, 0) + 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in list(self.data):
            target = value - num
            if target == num and self.data[target] > 1:
                return True
            elif target != num and target in self.data:
                return True
        return False    

#用list 实现：
#add时直接append
#find时先sort，然后用两个指针从头尾同时筛查
# add T(n) = O(1); Find T(n) = O(nlog(n)), S(n) = O(1)
class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """
    def __init__(self):
        self.data = []
    
    def add(self, number):
        # write your code here
        self.data.append(number)
        

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        self.data.sort()
        pl, pr = 0, len(self.data) - 1
        while pl < pr:
            cand = self.data[pl] + self.data[pr]
            if cand == value:
                return True
            elif cand < value:
                pl += 1
            else:
                pr -= 1
        return False
