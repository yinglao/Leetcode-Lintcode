## 本题关键在于在matrix中如何判断越界和如何调整步长“”转弯“，不会的话就要写很长的代码。
##53 - 56

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(n)] for i in  range(n)]
        if n == 0:
            return res
        d = 0
        v = 1
        while True:
            res[d][d] = v
            v += 1
            for i in range(d + 1, n - d):
                res[d][i] = v
                v += 1
            if v > n * n:
                return res
            for i in range(d + 1, n - d):
                res[i][n - d - 1] = v
                v += 1
            if v > n * n:
                return res    
            for i in range(d + 1, n - d):
                res[n - d - 1][n - 1 - i] = v
                v += 1
            if v > n * n:
                return res
            for i in range(d + 1, n - d - 1):
                res[n - 1 - i][d] = v
                v += 1
            if v > n * n:
                return res

            d += 1
            
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """        
        res = [[0 for j in range(n)] for i in  range(n)]
        if n == 0:
            return res
        di, dj = 0, 1
        i , j = 0, 0
        for v in range(1, n * n + 1):
            res[i][j] = v
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return res
        
