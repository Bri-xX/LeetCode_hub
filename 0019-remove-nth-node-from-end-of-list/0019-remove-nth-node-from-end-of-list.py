# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len = 1
        i = head
        while i.next != None:
            len = len + 1
            i = i.next
        
        if len == 1:
            head = None
        elif n == 1:
            j = head
            for i in range(len-2):
                j = j.next
            j.next = None
        
        elif len == n:
            j = head
            head = head.next
        else:
            j = head
            for i in range(len-n-1):
                j = j.next
            k = j.next.next
            j.next = k
        return head