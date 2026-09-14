# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 if l1 is not None else l2
        
        p = l1
        q = l2
        
        dummy = ListNode(-1)
        pointer = dummy
        carry = 0

        while p or q or carry:
            x = p.val  if p is not None else 0
            y = q.val if q is not None else 0
            addition = x + y + carry
            pointer.next = ListNode(addition%10)
            carry = addition//10
            if p:
                p = p.next
            if q:  
                q = q.next
            pointer = pointer.next

        return dummy.next 



        