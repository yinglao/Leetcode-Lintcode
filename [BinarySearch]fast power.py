#Calculate the a^n % b where a, b and n are all 32bit integers.
#
#Have you met this question in a real interview? 
#Example
#For 231 % 3 = 2
#
#For 1001000 % 1000 = 0
#
#关于同余运算的乘法关系：
#y = a % b
#(a * a) % b = (a % b) ** 2
#
#一般而言：
#f(x, y) % b = f(x%b, y%b) % b

#对加法和乘法都适用


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower2(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        if n % 2 == 1:
            y = a % b
            return (a * self.fastPower(2 * a * y - y * y, b, n // 2)) % b
        else:
            y = a % b
            return self.fastPower(2 * a * y - y * y, b, n // 2)
    
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        if n % 2 == 1:
            return (a * self.fastPower(a * a % b, b, n // 2)) % b
        else:
            return self.fastPower(a * a % b, b, n // 2)
