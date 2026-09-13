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

        p = head
        while p:
            hash[p].next = hash.get(p.next)
            hash[p].random = hash.get(p.random)
            p = p.next
        return hash[head]
        
        
            


        

        

            


        
        