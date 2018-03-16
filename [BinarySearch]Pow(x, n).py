#Implement pow(x, n).
#
# Notice
#You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.
#
#Have you met this question in a real interview? 
#Example
#Pow(2.1, 3) = 9.261
#Pow(0, 1) = 0
#Pow(1, 0) = 1

class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    
#T(n) = O(log n)
#S(n) = O(2)
#Recursion
    def myPow2(self, x, n):
        # write your code here
        def helper(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1.0 / helper(x, -n)
            if n == 1:
                return x
            if n % 2 == 0:
                return helper(x * x, n // 2)
            else:
                return helper(x * x, n // 2) * x
        return helper(x, n)
#T(n) = O(log n)
#S(n) = O(log n)
#Iteration       
    def myPow3(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        remains = []
        res = x
        while n > 1:
            if n % 2 == 1:
                remains.append(res)
            res = res * res
            n = n // 2
        for num in remains:
            res *= num
        return res
#T(n) = O(log n)
#S(n) = O(1)
#Iteration         
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        res = x
        factor = x
        while n > 1:
            if n % 2 == 1:
                res = res * factor
            res = res * factor
            factor = factor * factor
            n = n // 2
        return res
