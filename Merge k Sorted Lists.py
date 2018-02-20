#Merge k sorted linked lists and return it as one sorted list.
#
#Analyze and describe its complexity.
#
#Example
#Given lists:
#
#[
#  2->4->null,
#  null,
#  -1->null
#],
#return -1->2->4->null.
#
#
#
#将所有的linked list 先按 [val， linked list]的pair 存放成一个heap （O(k)）然后pop出来，将val放进result 中，如果linked list下一个不为None的话，则继续push回去，直到heap空为止
#



"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists or len(lists) == 0:
            return None
        import heapq
        i = 0
        l = len(lists)
        while i < l:
            if lists[i]:
                lists[i] = [lists[i].val, lists[i]]
            else:
                del lists[i]
                i -= 1
                l -= 1
            i += 1
        heapq.heapify(lists)
        head = ListNode(0)
        cur = head
        while lists:
            key, node = heapq.heappop(lists)
            #print key, node
            cur.next = ListNode(key)
            cur = cur.next
            if node.next:
                node = node.next
                heapq.heappush(lists, [node.val, node])
        return head.next
