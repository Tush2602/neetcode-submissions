# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        count = 0 
        while p :
            p = p.next
            count +=1

        if count == n:
            return head.next 
            
        p = head
        for i in range(0, count - n -1):
            p = p.next
            
        p.next = p.next.next
        p = head
        return p

        
        
        