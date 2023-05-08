# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtn = ListNode()
        cur = rtn
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
                
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return rtn.next
                