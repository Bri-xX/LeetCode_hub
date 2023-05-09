# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        mid = length // 2 + 1
        cur2 = head
        count = 1
        while count < mid:
            count += 1
            cur2 = cur2.next
        return cur2

