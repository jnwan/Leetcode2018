from .common import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carry = 0
        while(l1 is not None or l2 is not None):
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            newNode = ListNode(-1)
            if(carry + v1 + v2 >= 10):
                newNode.val = carry + v1 + v2 - 10;
                carry = 1
            else:
                newNode.val = carry + v1 + v2
                carry = 0
            cur.next = newNode
            cur = newNode
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if(carry == 1):
            cur.next = ListNode(1)

        return dummy.next

