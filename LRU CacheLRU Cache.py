#Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
#get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#

#功能：可以快速取出key - value： hashmap
#可以每次去除最远使用的的key - value
#
#利用priority heapq + hashmap实现。
#每一个heap的node存储一个list：[freq, key, value]。
#并用一个hashmap建立起key - [freq, key, value] 的对应关系，以上两个list是同一个。
class LRUCache2:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        import heapq
        self.data = {}
        self.hq = []
        self.maxcount = 0
        self.capacity = capacity
        self.date = 0

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        import heapq
        self.maxcount += 1
        if key in self.data:
            value = self.data[key][2]
            self.data[key][0] = self.maxcount
            heapq.heapify(self.hq)
        else: 
            return -1
        #print self.data
        return value
        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        import heapq
        self.maxcount += 1
        
        if key in self.data:
            self.data[key][2] = value
            self.data[key][0] = self.maxcount
            heapq.heapify(self.hq)
            #self.data[key][0] = 0
        else:
            self.data[key] = [self.maxcount, key, value]
            if len(self.hq) == self.capacity:
                f, k, v = heapq.heapreplace(self.hq, self.data[key])
                del self.data[k]
            else:
                heapq.heappush(self.hq, self.data[key])
                
                
class Node:
    def __init__(self, val):
        self.val = val #[None, key, val]
        self.next = None
        self.pre = None
    
#但以上算法每次get或者set都要对O(n)的复杂度
#
#更加合理的方法是采用linked list + hashmap
#每一个node的val 指向一个list[key, val],其next指向下一个最近常用的数。
#每次get都从hashmap中获取对应的value，用O(1) time。然后将对应的node放到队尾
#每次set：
#先检查hashmap中是否已经存在key，存在的话，直接修改其value，并将其对应的node移到linked list的队尾，结束
#如果不存在，在hashmap中创建一个新的key-[node, val]对，创建一个新的node，其val指向新的key-[node, val]对，然后再将新的key-[node, val]对中node改为这个node，
#
#检查linked list 的长度是否为capacity, 是的话，先将开头的node去掉，再从hashmap中去掉对应的key，然后将新建的node放到队尾，
#如果未达到capacity，直接将新的node放到队尾，然后更新linked list的长度        

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0
        self.data = {}
        
    
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.data:
            node, key, value = self.data[key]
            self.moveToTail(node)
            return value
        else:
            return -1
    
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.data:
            self.data[key][2] = value
            node = self.data[key][0]
            self.moveToTail(node)
        else:
            self.data[key] = [None, key, value]
            node = Node(self.data[key])
            self.data[key][0] = node
            if self.length == self.capacity:
                n,k,v = self.popFromHead().val
                self.addToTail(node)
                del self.data[k]
            else:
                self.addToTail(node)
                self.length += 1
        #if self.length >= self.capacity:
            #print self.length, self.capacity
        
        
    def moveToTail(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        
        self.tail.pre = node
        
    def popFromHead(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        return node
    
    def addToTail(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        node.pre.next = node
        self.tail.pre = node
            
