"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        p = head
        while p:
            next_node= p.next
            p.next = Node(p.val)
            p.next.next = next_node
            p = p.next.next
        
        p = head
        while p:
            if p.random is not None: 
                p.next.random = p.random.next
            else: 
                p.next.random= p.random
            p = p.next.next
        
        deepcopy = Node(-1)
        dummy = deepcopy
        p= head
        while p:
            dummy.next = p.next
            p.next = p.next.next
            p = p.next
            dummy = dummy.next

        return deepcopy.next
        
            


        

        

            


        
        