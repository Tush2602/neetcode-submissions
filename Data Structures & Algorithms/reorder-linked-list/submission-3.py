# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        sec= slow.next
        slow.next = None
        
        while sec:
            next_node= sec.next
            sec.next= prev
            prev = sec
            sec = next_node
        
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2 
        


        
