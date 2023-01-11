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
        node = head
        old_nodes = []
        new_nodes = []
        while node is not None:
            new_n = Node(node.val, node.next, None)
            node.next = new_n
            node = new_n.next
        node = head
        while node is not None:
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next
        new_head = head.next
        node = new_head
        while node.next is not None:
            node.next = node.next.next
            node = node.next
        return new_head