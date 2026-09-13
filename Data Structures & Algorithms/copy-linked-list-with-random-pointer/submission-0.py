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
        hash = {}
        while p:
            hash[p] = Node(p.val)
            p = p.next
        
        deepcopy = Node(-1)
        dummy = deepcopy
        p = head
        while p:
            deepcopy.next = hash[p]
            if p.random is None:
                deepcopy.next.random = None
            else:
                deepcopy.next.random = hash[p.random]
            p = p.next
            deepcopy = deepcopy.next
        return dummy.next
            


        

        

            


        
        