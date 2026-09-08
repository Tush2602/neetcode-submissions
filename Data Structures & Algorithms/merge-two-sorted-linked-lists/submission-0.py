# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is [] or list2 is []:
            return list2 if list1 is [] else list2  
        node = ListNode(0)
        curr = node

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val : 
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        if p1:
            curr.next= p1
        else:
            curr.next = p2

        return node.next
            

