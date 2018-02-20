#Implement strStr function in O(n + m) time.
#
#strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
#If target does not exist in source, just return -1.
#
#Have you met this question in a real interview? 
#Example
#Given source = abcdef, target = bcd, return 1
# http://www.lintcode.com/en/problem/strstr-ii/






class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    
    
#Rabin Karp 算法：
#最简单的做法是，逐段比较，比较O(n)次，每次用时O(m)，这样T(n) = O(mn)。RK算法是使用了hash的方法，将（大部分的）O(m)的比较时间转化成O(1)。换而言之，是充分利用可使用的整数的数量来“稀释”O(m)比较的密度。
#具体做法：
#首先算出target对应的hash int， 为了避免数字过大而造成的额外空间和额外时间的使用。我们再取一个合适的数字的模（hashsize），理论上而言会增加O(m)比较的密度，但能因此保证每次比较使用O(1)时间，是一种权衡的结果。
#
#算出前source前m位的hash int，与target进行比较，若不符合，则(hashint * 26 + source[m] - source[0])%hashsize获得下一段的hash int（费时O(1)），直到获得target的hash int。
#
#但从hash int 到源字符串并非一一对应，所以需要进行比较。而因为hashsize的“稀释”作用，这种一对多的对应关系并不多，可以认为是O(1)次，所以最终的费时为O(n + m)。



    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if len(target) == 0:
            return 0
        if len(source) == 0:
            return -1 
        
        m = len(target)
        n = len(source)
        hashsize = 1000000
        m26 = 1
        for i in range(m):
            m26 = (m26 * 26) % hashsize
        targetInt = 0
        for letter in target:
            targetInt = (targetInt * 26 + (ord(letter) - ord('a'))) % hashsize
        #print targetInt
        sourceInt = 0
        for i in range(m):
            sourceInt = (sourceInt * 26 + (ord(source[i]) - ord('a'))) % hashsize
        #print sourceInt
        if sourceInt == targetInt and source[:m] == target:
            return 0
        for i in range(m, n):
            sourceInt = ((sourceInt * 26) % hashsize + ((ord(source[i]) - ord('a')) % hashsize)) % hashsize
            sourceInt = (sourceInt - ((ord(source[i - m]) - ord('a')) * m26) % hashsize) % hashsize
            #print source[i-m]
            #print sourceInt
            if sourceInt == targetInt and source[i - m + 1 : i + 1] == target:
                return i - m + 1
        return -1
